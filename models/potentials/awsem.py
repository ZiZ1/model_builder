import numpy as np

##############################################################################
# Utility functions
##############################################################################

def theta(r, nu, r_min, r_max):
    return 0.25*(1. + np.tanh(nu*(r - r_min)))*(1. + np.tanh(nu*(r_max - r)))

def sigma_water(rhoi, rhoj, nu_sigma, rho_0):
    return 0.25*(1. - np.tanh(nu_sigma*(rhoi - rho_0)))*(1. - np.tanh(nu_sigma*(rhoj - rho_0)))

##############################################################################
# Backbone terms
##############################################################################

class Spring(object):
    # NOT TESTED
    def __init__(self, k, r0):
        """Harmonic potential 
        
        Used for V_connectivity and V_chain to maintain backbone geometry.
        
        Parameters
        ----------
        k : float
            Spring constant.
        r0 : float
            Equilibrium distance"""
        self.k = k
        self.r0 = r0

    def V(self, r):
        return self.k*((r - self.r0)**2)

class Chi(object):
    # NOT TESTED
    def __init__(self, lambda_chi=1., chi_0=-0.83):
        """Sidechain chirality potential

        Parameters
        ----------
        lambda_chi : opt, float
            The overall strength of the term in the Hamiltonian.
        nu : opt, float

        """
        self.lambda_chi
        self.chi_0

    def V(self, C_xyz, CA_xyz, CB_xyz, N_xyz):
        """
        Parameters
        ----------
        C_xyz : np.ndarray (3)
            Coordinates of the backbone C atom.
        CA_xyz : np.ndarray (3)
            Coordinates of the backbone CA atom.
        CB_xyz : np.ndarray (3)
            Coordinates of the CB atom.
        N_xyz : np.ndarray (3)
            Coordinates of the backbone N atom.
        """

        v1 = CA_xyz - C_xyz
        v2 = N_xyz - CA_xyz 
        v3 = CA_xyz - CB_xyz
        chi = np.dot(np.cross(v1, v2), v3) # Does this work vectorized?
        return self.lambda_chi*((chi - chi_0)**2)

class Rama(object):
    # NOT TESTED
    def __init__(self, lambda_rama=2., 
            W=[1.3149, 1.32016, 1.0264], sigma=[15.398, 49.0521, 49.0954],
            omega_phi=[0.15, 0.25, 0.65], phi0=[-1.74, -1.265, 1.041], 
            omega_psi=[0.65, 0.45, 0.25], psi0=[2.138, -0.318, 0.78]):
        self.lambda_rama = lambda_rama
        self.sigma = sigma
        self.omega_phi = omega_phi
        self.phi0 = phi0
        self.omega_psi = omega_psi
        self.psi0 = psi0

    def V(self, phi, psi):
        V = np.zeros(phi.shape[0], float)
        for i in range(len(self.W)):
            V += -self.lambda_rama*W[i]*np.exp(-sigma[i]*(
                    self.omega_phi[i]*(np.cos(phi - self.phi0[i]) - 1.)**2 +\
                    self.omega_psi[i]*(np.cos(psi - self.psi0[i]) - 1.)**2))
        return V

class Helix(object):

    def __init__(self, lambda_helix=1.5,
            gamma_protein=2., gamma_water=-1., nu=70., nu_sigma=7.,
            rho_0=3., r_ON=0.298, r_OH=0.206, sigma_ON=0.068, sigma_OH=0.076):
        """Alpha helical interaction
    
        Parameters
        ----------
        lambda_direct : opt, float
            The overall strength of the term in the Hamiltonian.
        
        """

        self.lambda_helix = lambda_helix
        self.gamma_protein = gamma_protein
        self.gamma_water = gamma_water
        self.nu = nu
        self.nu_sigma = nu_sigma
        self.rho_0 = rho_0
        self.r_ON_0 = r_ON
        self.r_OH_0 = r_OH
        self.sigma_ON = sigma_ON
        self.sigma_OH = sigma_OH

    def V(self, r_ON, r_OH, rhoi, rhoj, fai, fai_4):
        return (fai + fai_4)*self.gauss_well(r_ON, r_OH)*(
                self.gamma_water*sigma_water(rhoi, rhoj, self.nu_sigma, self.rho_0) +\
                self.gamma_protein*(1. - sigma_water(rhoi, rhoj, self.nu_sigma, self.rho_0)))
    
    def gauss_well(self, r_ON, r_OH):  
        return -self.lambda_helix*np.exp(-(((r_ON - self.r_ON_0)**2)/(2.*(self.sigma_ON**2))) -\
                                          (((r_OH - self.r_OH_0)**2)/(2.*(self.sigma_OH**2))))

##############################################################################
# Contact terms
##############################################################################

class DirectContact(object):

    def __init__(self, lambda_direct=1, nu=50., r_min=0.45, r_max=0.65):
        """Direct contact interaction
        
        Parameters
        ----------
        lambda_direct : opt, float
            The overall strength of the term in the Hamiltonian.
        nu : opt, float
            Coefficient that sets how quickly the contact well switches
            between on and off.
        r_min : opt, float
            The minimum of the contact well.
        r_max : opt, float
            The maximum of the contact well.
            
        """
        self.lambda_direct = lambda_direct
        self.nu = nu
        self.r_min = r_min
        self.r_max = r_max

    def V(self, r, gamma_direct): 
        return -self.lambda_direct*gamma_direct*self.theta_I(r)

    def dVdgamma_direct(self, r):
        return self.theta_I(r)

    def theta_I(self, r):
        return theta(r, self.nu, self.r_min, self.r_max)

class WaterMediatedContact(object):
    
    def __init__(self, lambda_water=1., nu=50., nu_sigma=7., r_min=0.65, r_max=0.95, rho_0=2.6):
        """Water- or protein-mediated contact interaction
        
        Parameters
        ----------
        lambda_water : opt, float
            The overall strength of the term in the Hamiltonian.
        nu : opt, float
            Coefficient that sets how quickly the contact well switches
            between on and off.
        nu_sigma : opt, float
            Coefficient that sets how fast the contact switches from 
            water-mediated to protein-mediated based on the local densities of
            the residues involved.
        r_min : opt, float
            The minimum of the contact well.
        r_max : opt, float
            The maximum of the contact well.
            
        """
        self.lambda_water = lambda_water
        self.nu = nu
        self.nu_sigma = nu_sigma
        self.r_min = r_min
        self.r_max = r_max
        self.rho_0 = rho_0

    def V(self, r, rhoi, rhoj, gamma_water, gamma_protein): 
        """Water- or protein-mediated contact interaction
        
        Parameters
        ----------
        r : np.ndarray (n_frames)
            Distance between sidechain CB's involved in interaction. If one or
            both residues are glycine then the CA atom is used instead.
        rhoi : np.ndarray (n_frames)
            Local protein density around residue i.
        rhoj : np.ndarray (n_frames)
            Local protein density around residue j.
        gamma_water : float
            The strength of the water-mediated interaction between residues i
            and j.
        gamma_protein : float
            The strength of the protein-mediated interaction between residues i
            and j.
        
        """
        return -self.lambda_water*(gamma_water*self.dVdgamma_water(r, rhoi, rhoj) +\
                                gamma_protein*self.dVdgamma_protein(r, rhoi, rhoj))

    def dVdgamma_water(self, r, rhoi, rhoj):
        return self.theta_II(r)*sigma_water(rhoi, rhoj, self.nu_sigma, self.rho_0)

    def dVdgamma_protein(self, r, rhoi, rhoj):
        return self.theta_II(r)*(1. - sigma_water(rhoi, rhoj, self.nu_sigma, self.rho_0))

    def theta_II(self, r):
        return theta(r, self.nu, self.r_min, self.r_max)

    
class Burial(object):
    def __init__(self, lambda_burial=1., nu=4., rho1_lims=[0.0, 3.], rho2_lims=[3., 6.], rho3_lims=[6., 9.]):
        """One-body burial potential

        The burial potential assigns an energy for being in (1) low, (2)
        medium, or (3) high protein density. 

        Parameters
        ----------
        lambda_burial : opt, float
            The overall strength of the term in the Hamiltonian.
        nu : opt, float
            Coefficient that sets how quickly the burial well switches between on and off.
        rho1_lims : opt, list (2)
            The density limits of the low-density well.
        rho2_lims : opt, list (2)
            The density limits of the medium-density well.
        rho3_lims : opt, list (2)
            The density limits of the high-density well.

        """

        self.label = "BURIAL"
        self.lambda_burial = lambda_burial
        self.nu = nu
        self.rho_lims = [ rho1_lims, rho2_lims, rho3_lims ]

    def describe(self):
        return "{} potential : lambda_burial {} nu = {}, rho_lims = {}".format(
                self.label, self.lambda_burial, self.nu, self.rho_lims.__repr__())

    def V(self, rhoi, gamma_burials):
        """Burial potential
        
        Parameters
        ----------
        rhoi : np.ndarray 
            Vector that contains the local protein density at site i.
        gamma_burials : list (3)
            Residue specific burial coefficients for residue type i to be in
            low-, medium-, or high-density environment.
    
        """
        V = np.zeros(rhoi.shape[0])
        for i in range(3):
            V += -self.lambda_burial*gamma_burials[i]*self.burial_theta(
                        rhoi, self.nu, self.rho_lims[i][0], self.rho_lims[i][1])
        return V

    def burial_theta(self, rhoi, nu, rho_min, rho_max):
        #return  0.5*np.tanh(nu*(rhoi - rho_min))*np.tanh(nu*(rhoi- rho_max))
        return  0.5*(np.tanh(nu*(rhoi - rho_min)) + np.tanh(nu*(rho_max - rhoi)))

AWSEM_POTENTIALS = {"DIRECT":DirectContact,
                "WATER":WaterMediatedContact,
                "BURIAL":Burial, 
                "HELIX":Helix,
                "CHI":Chi}
