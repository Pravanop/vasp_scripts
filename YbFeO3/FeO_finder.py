from pymatgen.analysis.bond_valence import BVAnalyzer, calculate_bv_sum
from pymatgen.core.structure import Structure, Molecule
from matminer.featurizers.site import CrystalNNFingerprint
from matminer.featurizers.structure import SiteStatsFingerprint

ssf = SiteStatsFingerprint(
        CrystalNNFingerprint.from_preset('ops', distance_cutoffs=None, x_diff_weight=0),
        stats=('mean', 'std_dev', 'minimum', 'maximum'))

np.array(ssf.featurize(s))