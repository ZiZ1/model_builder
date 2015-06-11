# coding=utf-8
""" Holding properties of residues"""

import numpy as np

"""Masses in atomic mass units"""
residue_mass = {'ALA':   89.0935, 'ARG':  174.2017, 'ASN':  132.1184,
                'ASP':  133.1032, 'CYS':  121.1590, 'GLN':  146.1451,
                'GLU':  147.1299, 'GLY':   75.0669, 'HIS':  155.1552,
                'ILE':  131.1736, 'LEU':  131.1736, 'LYS':  146.1882,
                'MET':  149.2124, 'PHE':  165.1900, 'PRO':  115.1310,
                'SER':  105.0930, 'THR':  119.1197, 'TRP':  204.2262,
                'TYR':  181.1894, 'VAL':  117.1469, 'SOL':   18.0150}

"""Converting from three letter code to one letter FASTA code."""
residue_code = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N',
                'ASP': 'D', 'CYS': 'C', 'GLN': 'Q',
                'GLU': 'E', 'GLY': 'G', 'HIS': 'H',
                'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
                'MET': 'M', 'PHE': 'F', 'PRO': 'P',
                'SER': 'S', 'THR': 'T', 'TRP': 'W',
                'TYR': 'Y', 'VAL': 'V'}

"""Source: Partial molar volumes of proteins: amino acid side-chain
contributions derived from the partial molar volumes of some tripeptide
Atomic radii in nanometers"""
residue_radii = {'ALA': 0.1844827, 'ARG': 0.3134491, 'ASN': 0.2477519,
                'ASP': 0.2334602, 'CYS': 0.2276212, 'GLN': 0.2733978,
                'GLU': 0.2639170, 'GLY': 0.0000000, 'HIS': 0.2835556,
                'ILE': 0.2889931, 'LEU': 0.2887070, 'LYS': 0.2937731,
                'MET': 0.2916368, 'PHE': 0.3140150, 'PRO': 0.2419109,
                'SER': 0.1936102, 'THR': 0.2376198, 'TRP': 0.3422321,
                'TYR': 0.3168939, 'VAL': 0.2619603, 'AVERAGE': 0.2683678}

residues_alpha = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN',
                  'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS',
                  'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP',
                  'TYR', 'VAL']

residues_hydrophobicity = ['CYS', 'MET', 'PHE', 'ILE', 'LEU',
                           'VAL', 'TRP', 'TYR', 'ALA', 'GLY',
                           'THR', 'SER', 'GLN', 'ASN', 'GLU', 
                           'ASP', 'HIS', 'ARG', 'LYS', 'PRO']

# Alphabetically ordered
miyazawa_jernigan_mohit = np.array([
[-0.12,   0.24,   0.15,   0.27,  -0.33,   0.22,   0.38,  -0.08,   0.07,  -0.37,  -0.38,   0.41,  -0.27,  -0.36,   0.15,   0.10,   0.04,  -0.27,  -0.20,  -0.32],
[ 0.24,   0.19,   0.10,  -0.24,   0.08,   0.09,  -0.22,   0.09,   0.05,   0.00,  -0.04,   0.66,   0.03,  -0.05,   0.17,   0.16,   0.11,  -0.21,  -0.25,   0.08],
[ 0.15,   0.10,  -0.06,   0.02,  -0.01,   0.06,   0.12,  -0.01,   0.00,   0.14,   0.04,   0.22,   0.04,  -0.01,   0.18,   0.09,   0.04,  -0.10,  -0.11,   0.12],
[ 0.27,  -0.24,   0.02,   0.29,   0.12,   0.24,   0.44,   0.11,  -0.10,   0.22,   0.27,  -0.01,   0.30,   0.18,   0.33,   0.10,   0.11,   0.07,  -0.07,   0.36],
[-0.33,   0.08,  -0.01,   0.12,  -1.19,  -0.07,   0.20,  -0.31,  -0.36,  -0.64,  -0.65,   0.33,  -0.61,  -0.67,  -0.18,  -0.13,  -0.15,  -0.66,  -0.39,  -0.59],
[ 0.22,   0.09,   0.06,   0.24,  -0.07,   0.20,   0.27,   0.13,   0.15,  -0.01,  -0.04,   0.28,  -0.06,  -0.11,   0.17,   0.22,   0.12,  -0.02,  -0.14,   0.08],
[ 0.38,  -0.22,   0.12,   0.44,   0.20,   0.27,   0.46,   0.32,   0.00,   0.17,   0.17,  -0.06,   0.12,   0.14,   0.37,   0.18,   0.16,   0.00,  -0.08,   0.26],
[-0.08,   0.09,  -0.01,   0.11,  -0.31,   0.13,   0.32,  -0.29,   0.00,  -0.13,  -0.16,   0.29,  -0.17,  -0.19,   0.02,  -0.01,  -0.04,  -0.25,  -0.22,  -0.15],
[ 0.07,   0.05,   0.00,  -0.10,  -0.36,   0.15,   0.00,   0.00,  -0.40,  -0.13,  -0.18,   0.38,  -0.29,  -0.34,   0.01,   0.04,  -0.03,  -0.37,  -0.30,  -0.06],
[-0.37,   0.00,   0.14,   0.22,  -0.64,  -0.01,   0.17,  -0.13,  -0.13,  -0.74,  -0.81,   0.24,  -0.66,  -0.73,  -0.05,   0.03,  -0.15,  -0.60,  -0.49,  -0.67],
[-0.38,  -0.04,   0.04,   0.27,  -0.65,  -0.04,   0.17,  -0.16,  -0.18,  -0.81,  -0.84,   0.22,  -0.70,  -0.80,  -0.12,  -0.02,  -0.15,  -0.62,  -0.55,  -0.74],
[ 0.41,   0.66,   0.22,  -0.01,   0.33,   0.28,  -0.06,   0.29,   0.38,   0.24,   0.22,   0.76,   0.29,   0.19,   0.47,   0.36,   0.33,   0.09,  -0.05,   0.29],
[-0.27,   0.03,   0.04,   0.30,  -0.61,  -0.06,   0.12,  -0.17,  -0.29,  -0.66,  -0.70,   0.29,  -0.70,  -0.83,  -0.13,   0.05,  -0.11,  -0.73,  -0.56,  -0.51],
[-0.36,  -0.05,  -0.01,   0.18,  -0.67,  -0.11,   0.14,  -0.19,  -0.34,  -0.73,  -0.80,   0.19,  -0.83,  -0.88,  -0.19,  -0.12,  -0.15,  -0.68,  -0.58,  -0.67],
[ 0.15,   0.17,   0.18,   0.33,  -0.18,   0.17,   0.37,   0.02,   0.01,  -0.05,  -0.12,   0.47,  -0.13,  -0.19,   0.11,   0.20,   0.13,  -0.37,  -0.25,  -0.05],
[ 0.10,   0.16,   0.09,   0.10,  -0.13,   0.22,   0.18,  -0.01,   0.04,   0.03,  -0.02,   0.36,   0.05,  -0.12,   0.20,   0.05,   0.04,  -0.01,  -0.08,   0.04],
[ 0.04,   0.11,   0.04,   0.11,  -0.15,   0.12,   0.16,  -0.04,  -0.03,  -0.15,  -0.15,   0.33,  -0.11,  -0.15,   0.13,   0.04,   0.03,  -0.02,  -0.09,  -0.07],
[-0.27,  -0.21,  -0.10,   0.07,  -0.66,  -0.02,   0.00,  -0.25,  -0.37,  -0.60,  -0.62,   0.09,  -0.73,  -0.68,  -0.37,  -0.01,  -0.02,  -0.64,  -0.49,  -0.51],
[-0.20,  -0.25,  -0.11,  -0.07,  -0.39,  -0.14,  -0.08,  -0.22,  -0.30,  -0.49,  -0.55,  -0.05,  -0.56,  -0.58,  -0.25,  -0.08,  -0.09,  -0.49,  -0.45,  -0.38],
[-0.32,   0.08,   0.12,   0.36,  -0.59,   0.08,   0.26,  -0.15,  -0.06,  -0.67,  -0.74,   0.29,  -0.51,  -0.67,  -0.05,   0.04,  -0.07,  -0.51,  -0.38,  -0.65]])


# Alphabetically ordered
miyazawa_jernigan_contact_weight_claude = np.array([
[ 2.72, 1.83, 1.84, 1.70, 3.57, 1.89, 1.51, 2.31, 2.41, 4.58, 4.91, 1.31, 3.94, 4.81, 2.03, 2.01, 2.32, 3.82, 3.36, 4.04],
[ 1.83, 1.55, 1.64, 2.29, 2.57, 1.80, 2.27, 1.72, 2.16, 3.63, 4.03, 0.59, 3.12, 3.98, 1.70, 1.62, 1.90, 3.41, 3.16, 3.07],
[ 1.84, 1.64, 1.68, 1.68, 2.59, 1.71, 1.51, 1.74, 2.08, 3.24, 3.74, 1.21, 2.95, 3.75, 1.53, 1.58, 1.88, 3.07, 2.76, 2.83],
[ 1.70, 2.29, 1.68, 1.21, 2.41, 1.46, 1.02, 1.59, 2.32, 3.17, 3.40, 1.68, 2.57, 3.48, 1.33, 1.63, 1.80, 2.84, 2.76, 2.48],
[ 3.57, 2.57, 2.59, 2.41, 5.44, 2.85, 2.27, 3.16, 3.60, 5.50, 5.83, 1.95, 4.99, 5.80, 3.07, 2.86, 3.11, 4.95, 4.16, 4.96],
[ 1.89, 1.80, 1.71, 1.46, 2.85, 1.54, 1.42, 1.66, 1.98, 3.67, 4.04, 1.29, 3.30, 4.10, 1.73, 1.49, 1.90, 3.11, 2.97, 3.07],
[ 1.51, 2.27, 1.51, 1.02, 2.27, 1.42, 0.91, 1.22, 2.15, 3.27, 3.59, 1.80, 2.89, 3.56, 1.26, 1.48, 1.74, 2.99, 2.79, 2.67],
[ 2.31, 1.72, 1.74, 1.59, 3.16, 1.66, 1.22, 2.24, 2.15, 3.78, 4.16, 1.15, 3.39, 4.13, 1.87, 1.82, 2.08, 3.42, 3.01, 3.38],
[ 2.41, 2.16, 2.08, 2.32, 3.60, 1.98, 2.15, 2.15, 3.05, 4.14, 4.54, 1.35, 3.98, 4.77, 2.25, 2.11, 2.42, 3.98, 3.52, 3.58],
[ 4.58, 3.63, 3.24, 3.17, 5.50, 3.67, 3.27, 3.78, 4.14, 6.54, 7.04, 3.01, 6.02, 6.84, 3.76, 3.52, 4.03, 5.78, 5.25, 6.05],
[ 4.91, 4.03, 3.74, 3.40, 5.83, 4.04, 3.59, 4.16, 4.54, 7.04, 7.37, 3.37, 6.41, 7.28, 4.20, 3.92, 4.34, 6.14, 5.67, 6.48],
[ 1.31, 0.59, 1.21, 1.68, 1.95, 1.29, 1.80, 1.15, 1.35, 3.01, 3.37, 0.12, 2.48, 3.36, 0.97, 1.05, 1.31, 2.69, 2.60, 2.49],
[ 3.94, 3.12, 2.95, 2.57, 4.99, 3.30, 2.89, 3.39, 3.98, 6.02, 6.41, 2.48, 5.46, 6.56, 3.45, 3.03, 3.51, 5.55, 4.91, 5.32],
[ 4.81, 3.98, 3.75, 3.48, 5.80, 4.10, 3.56, 4.13, 4.77, 6.84, 7.28, 3.36, 6.56, 7.26, 4.25, 4.02, 4.28, 6.16, 5.66, 6.29],
[ 2.03, 1.70, 1.53, 1.33, 3.07, 1.73, 1.26, 1.87, 2.25, 3.76, 4.20, 0.97, 3.45, 4.25, 1.75, 1.57, 1.90, 3.73, 3.19, 3.32],
[ 2.01, 1.62, 1.58, 1.63, 2.86, 1.49, 1.48, 1.82, 2.11, 3.52, 3.92, 1.05, 3.03, 4.02, 1.57, 1.67, 1.96, 2.99, 2.78, 3.05],
[ 2.32, 1.90, 1.88, 1.80, 3.11, 1.90, 1.74, 2.08, 2.42, 4.03, 4.34, 1.31, 3.51, 4.28, 1.90, 1.96, 2.12, 3.22, 3.01, 3.46],
[ 3.82, 3.41, 3.07, 2.84, 4.95, 3.11, 2.99, 3.42, 3.98, 5.78, 6.14, 2.69, 5.55, 6.16, 3.73, 2.99, 3.22, 5.06, 4.66, 5.18],
[ 3.36, 3.16, 2.76, 2.76, 4.16, 2.97, 2.79, 3.01, 3.52, 5.25, 5.67, 2.60, 4.91, 5.66, 3.19, 2.78, 3.01, 4.66, 4.17, 4.62],
[ 4.04, 3.07, 2.83, 2.48, 4.96, 3.07, 2.67, 3.38, 3.58, 6.05, 6.48, 2.49, 5.32, 6.29, 3.32, 3.05, 3.46, 5.18, 4.62, 5.52]])

# Alphabetically ordered. 
awsem_direct_contact_gammas = np.array([
[  0.720080, -0.270290,  -0.259680,  -0.402220,   0.620530,  -0.244690,  -0.348510,  -0.113910,  -0.125110,   1.000000,   1.000000,  -0.451560,   0.507320,   0.568570,  -0.534590,  -0.206250,   0.080040,   0.396630,   0.111830,   0.917950],
[ -0.270290, -0.641720,  -0.281130,   0.409220,  -0.400380,  -0.209180,  -0.033780,  -0.328640,  -0.534140,  -0.136290,  -0.251040,  -0.955880,  -0.016960,  -0.175140,  -0.824930,  -0.331090,  -0.234460,  -0.299730,   0.140870,  -0.169600],
[ -0.259680, -0.281130,   0.164030,   0.024840,  -0.092170,  -0.193760,  -0.562360,  -0.144930,  -0.069100,  -0.724360,  -0.578350,  -0.454760,  -0.595000,  -0.522340,  -0.694000,  -0.021710,  -0.314120,  -0.373100,  -0.274600,  -0.591150],
[ -0.402220,  0.409220,   0.024840,  -0.572840,  -0.369600,  -0.393600,  -0.847440,  -0.304370,  -0.084570,  -0.721130,  -0.782620,   0.105590,  -0.578660,  -0.762530,  -0.816750,  -0.034430,  -0.219790,  -0.739460,  -0.781870,  -0.736310],
[  0.620530, -0.400380,  -0.092170,  -0.369600,   0.977650,  -0.434360,  -0.357920,   0.433920,   0.694100,   0.702920,   0.977650,  -0.575230,   0.297840,   0.851080,   0.085830,   0.471820,  -0.175140,   0.100470,   0.865350,   0.950440],
[ -0.244690, -0.209180,  -0.193760,  -0.393600,  -0.434360,  -0.287070,  -0.491660,  -0.369150,  -0.717500,  -0.431820,  -0.294620,  -0.491360,  -0.332390,  -0.345180,  -0.596080,  -0.341940,  -0.032120,  -0.556030,  -0.205660,  -0.275010],
[ -0.348510, -0.033780,  -0.562360,  -0.847440,  -0.357920,  -0.491660,  -0.857940,  -0.548380,  -0.503420,  -0.493860,  -0.556730,   0.130180,  -0.768200,  -0.749760,  -0.777100,  -0.307940,   0.047860,  -0.459950,  -0.315650,  -0.381750],
[ -0.113910, -0.328640,  -0.144930,  -0.304370,   0.433920,  -0.369150,  -0.548380,   0.370360,  -0.423550,   0.037100,  -0.219210,  -0.482800,   0.133610,  -0.052230,  -0.415650,   0.023300,  -0.138350,   0.038610,   0.149100,  -0.113070],
[ -0.125110, -0.534140,  -0.069100,  -0.084570,   0.694100,  -0.717500,  -0.503420,  -0.423550,  -0.158360,  -0.295070,   0.082500,  -0.553100,   0.196090,   0.368320,  -0.603340,  -0.028730,  -0.092810,  -0.012180,   0.260840,   0.155480],
[  1.000000, -0.136290,  -0.724360,  -0.721130,   0.702920,  -0.431820,  -0.493860,   0.037100,  -0.295070,   0.977650,   0.977650,  -0.710050,   0.744110,   0.877760,  -0.430510,  -0.431150,  -0.024320,   0.819440,   0.896230,   0.977650],
[  1.000000, -0.251040,  -0.578350,  -0.782620,   0.977650,  -0.294620,  -0.556730,  -0.219210,   0.082500,   0.977650,   0.977650,  -0.662470,   0.852470,   0.792690,  -0.543030,  -0.341180,   0.010570,   0.977650,   0.693170,   0.977650],
[ -0.451560, -0.955880,  -0.454760,   0.105590,  -0.575230,  -0.491360,   0.130180,  -0.482800,  -0.553100,  -0.710050,  -0.662470,  -0.967900,  -0.704820,  -0.663430,  -1.000000,  -0.621540,  -0.547860,  -0.397950,  -0.180360,  -0.618030],
[  0.507320, -0.016960,  -0.595000,  -0.578660,   0.297840,  -0.332390,  -0.768200,   0.133610,   0.196090,   0.744110,   0.852470,  -0.704820,   0.517480,   0.688710,  -0.496770,  -0.334410,  -0.093070,   0.116720,   0.635000,   0.628080],
[  0.568570, -0.175140,  -0.522340,  -0.762530,   0.851080,  -0.345180,  -0.749760,  -0.052230,   0.368320,   0.877760,   0.792690,  -0.663430,   0.688710,   0.977650,  -0.217920,  -0.267220,  -0.155050,   0.669960,   0.615280,   0.783650],
[ -0.534590, -0.824930,  -0.694000,  -0.816750,   0.085830,  -0.596080,  -0.777100,  -0.415650,  -0.603340,  -0.430510,  -0.543030,  -1.000000,  -0.496770,  -0.217920,  -0.507190,  -0.561690,  -0.470210,   0.011610,   0.058920,  -0.327550],
[ -0.206250, -0.331090,  -0.021710,  -0.034430,   0.471820,  -0.341940,  -0.307940,   0.023300,  -0.028730,  -0.431150,  -0.341180,  -0.621540,  -0.334410,  -0.267220,  -0.561690,  -0.104390,  -0.095870,  -0.320550,  -0.299430,  -0.249360],
[  0.080040, -0.234460,  -0.314120,  -0.219790,  -0.175140,  -0.032120,   0.047860,  -0.138350,  -0.092810,  -0.024320,   0.010570,  -0.547860,  -0.093070,  -0.155050,  -0.470210,  -0.095870,   0.160540,  -0.437650,  -0.223700,   0.181280],
[  0.396630, -0.299730,  -0.373100,  -0.739460,   0.100470,  -0.556030,  -0.459950,   0.038610,  -0.012180,   0.819440,   0.977650,  -0.397950,   0.116720,   0.669960,   0.011610,  -0.320550,  -0.437650,   0.074860,   0.212180,   0.517340],
[  0.111830,  0.140870,  -0.274600,  -0.781870,   0.865350,  -0.205660,  -0.315650,   0.149100,   0.260840,   0.896230,   0.693170,  -0.180360,   0.635000,   0.615280,   0.058920,  -0.299430,  -0.223700,   0.212180,   0.545870,   0.617310],
[  0.917950, -0.169600,  -0.591150,  -0.736310,   0.950440,  -0.275010,  -0.381750,  -0.113070,   0.155480,   0.977650,   0.977650,  -0.618030,   0.628080,   0.783650,  -0.327550,  -0.249360,   0.181280,   0.517340,   0.617310,   0.977650]])

def get_awsem_direct_contact_gamma(resA,resB):
    """ Returns direct contact interactions strength from AWSEM

    From the supplementary information of: 
    Davtyan, A.; Schafer, N. P.; Zheng, W.; Clementi, C.; Peter, G.
    Supplemental - AWSEM-MD : Protein Structure Prediction Using Coarse-Grained
    Physical Potentials and Bioinformatically Based Local Structure Biasing
    Description of the Coarse-Grained Protein Chain. J. Phys. Chem. B 2012, 1–22.
    """
    idx_a = residues_alpha.index(resA)
    idx_b = residues_alpha.index(resB)
    return awsem_direct_contact_gammas[idx_a,idx_b]
