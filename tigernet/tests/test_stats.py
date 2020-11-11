"""Testing for tigernet.py
"""

import tigernet
import unittest
import numpy
import geopandas
from shapely.geometry import LineString

# get the roads shapefile as a GeoDataFrame
bbox = (-84.279, 30.480, -84.245, 30.505)
f = "zip://test_data/Edges_Leon_FL_2010.zip!Edges_Leon_FL_2010.shp"
gdf = geopandas.read_file(f, bbox=bbox)
gdf = gdf.to_crs("epsg:2779")

# filter out only roads
yes_roads = gdf["ROADFLG"] == "Y"
roads = gdf[yes_roads].copy()

# Tiger attributes primary and secondary
ATTR1, ATTR2 = "MTFCC", "TLID"

# segment welding and splitting stipulations --------------------------------------------
INTRST = "S1100"  # interstates mtfcc code
RAMP = "S1630"  # ramp mtfcc code
SERV_DR = "S1640"  # service drive mtfcc code
SPLIT_GRP = "FULLNAME"  # grouped by this variable
SPLIT_BY = [RAMP, SERV_DR]  # split interstates by ramps & service
SKIP_RESTR = True  # no weld retry if still MLS


##########################################################################################
# Synthetic testing
##########################################################################################


class TestNeworkStatsBarb(unittest.TestCase):
    def setUp(self):
        lat = tigernet.generate_lattice(n_hori_lines=1, n_vert_lines=1, wbox=True)
        lat = lat[~lat["SegID"].isin([3, 5, 8])]
        rec = {
            "geometry": LineString(((4.5, 9), (4.5, 13.5))),
            "SegID": 13,
            "MTFCC": "S1400",
        }
        barb = lat.append(rec, ignore_index=True)

        # full network
        self.network = tigernet.Network(s_data=barb.copy())
        self.network.calc_net_stats()

        # simplified network
        self.graph = self.network.simplify_network()
        self.graph.calc_net_stats()

    def test_barb_network_sinuosity(self):
        known_sinuosity = [1.0] * 10
        observed_sinuosity = list(self.network.s_data["sinuosity"])
        self.assertEqual(observed_sinuosity, known_sinuosity)

    def test_barb_network_sinuosity_stats(self):
        known_max = 1.0
        observed_max = self.network.max_sinuosity
        self.assertEqual(observed_max, known_max)

        known_min = 1.0
        observed_min = self.network.min_sinuosity
        self.assertEqual(observed_min, known_min)

        known_mean = 1.0
        observed_mean = self.network.mean_sinuosity
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.0
        observed_std = self.network.std_sinuosity
        self.assertEqual(observed_std, known_std)

    def test_barb_graph_sinuosity(self):
        known_sinuosity = [2.23606797749979, numpy.inf, 1.0]
        observed_sinuosity = list(self.graph.s_data["sinuosity"])
        self.assertEqual(observed_sinuosity, known_sinuosity)

    def test_barb_graph_sinuosity_stats(self):
        known_max = 2.23606797749979
        observed_max = self.graph.max_sinuosity
        self.assertEqual(observed_max, known_max)

        known_min = 1.0
        observed_min = self.graph.min_sinuosity
        self.assertEqual(observed_min, known_min)

        known_mean = 1.8240453183331933
        observed_mean = self.graph.mean_sinuosity
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.71364417954618
        observed_std = self.graph.std_sinuosity
        self.assertEqual(observed_std, known_std)

    def test_barb_network_node_degree_stats(self):
        known_max = 4
        observed_max = self.network.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.network.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 2.0
        observed_mean = self.network.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.816496580927726
        observed_std = self.network.std_node_degree
        self.assertEqual(observed_std, known_std)

    def test_barb_graph_node_degree_stats(self):
        known_max = 4
        observed_max = self.graph.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.graph.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 2.0
        observed_mean = self.graph.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 1.7320508075688772
        observed_std = self.graph.std_node_degree
        self.assertEqual(observed_std, known_std)


class TestNeworkStatsSineLine(unittest.TestCase):
    def setUp(self):
        sine = tigernet.generate_sine_lines()
        sine = tigernet.generate_sine_lines()
        sine = sine[sine["SegID"].isin([0, 1, 2, 3])]

        # full network
        self.network = tigernet.Network(s_data=sine.copy())
        self.network.calc_net_stats()

        # simplified network
        self.graph = self.network.simplify_network()
        self.graph.calc_net_stats()

    def test_sine_network_sinuosity(self):
        known_sinuosity = [
            1.1913994275103448,
            1.0377484765201541,
            1.0714252226602858,
            1.1885699897294775,
        ]
        observed_sinuosity = list(self.network.s_data["sinuosity"])
        self.assertEqual(observed_sinuosity, known_sinuosity)

    def test_sine_network_sinuosity_stats(self):
        known_max = 1.1913994275103448
        observed_max = self.network.max_sinuosity
        self.assertEqual(observed_max, known_max)

        known_min = 1.0377484765201541
        observed_min = self.network.min_sinuosity
        self.assertEqual(observed_min, known_min)

        known_mean = 1.1222857791050656
        observed_mean = self.network.mean_sinuosity
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.07938019212245889
        observed_std = self.network.std_sinuosity
        self.assertEqual(observed_std, known_std)

    def test_sine_graph_sinuosity(self):
        known_sinuosity = [1.2105497715794307, 1.2105497715794304]
        observed_sinuosity = list(self.graph.s_data["sinuosity"])
        self.assertEqual(observed_sinuosity, known_sinuosity)

    def test_sine_graph_sinuosity_stats(self):
        known_max = 1.2105497715794307
        observed_max = self.graph.max_sinuosity
        self.assertEqual(observed_max, known_max)

        known_min = 1.2105497715794304
        observed_min = self.graph.min_sinuosity
        self.assertEqual(observed_min, known_min)

        known_mean = 1.2105497715794304
        observed_mean = self.graph.mean_sinuosity
        self.assertEqual(observed_mean, known_mean)

        known_std = 2.220446049250313e-16
        observed_std = self.graph.std_sinuosity
        self.assertEqual(observed_std, known_std)

    def test_sine_network_node_degree_stats(self):
        known_max = 2
        observed_max = self.network.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.network.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 1.3333333333333333
        observed_mean = self.network.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.5163977794943223
        observed_std = self.network.std_node_degree
        self.assertEqual(observed_std, known_std)

    def test_sine_graph_node_degree_stats(self):
        known_max = 1
        observed_max = self.graph.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.graph.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 1.0
        observed_mean = self.graph.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.0
        observed_std = self.graph.std_node_degree
        self.assertEqual(observed_std, known_std)


class TestNeworkConnectivityLattice1x1(unittest.TestCase):
    def setUp(self):
        lat1 = tigernet.generate_lattice(n_hori_lines=1, n_vert_lines=1)
        kws = {"n_hori_lines": 1, "n_vert_lines": 1, "bounds": [6, 6, 8, 8]}
        lat2 = tigernet.generate_lattice(**kws)
        self.lats = lat1.append(lat2)
        self.lats.reset_index(drop=True, inplace=True)

    def test_lattice_network_wcomps_connectivity(self):
        # with recorded components
        net_wcomps = tigernet.Network(s_data=self.lats.copy(), record_components=True)
        net_wcomps.calc_net_stats(conn_stat="all")

        known_alpha = 0.0
        observed_alpha = net_wcomps.alpha
        self.assertEqual(observed_alpha, known_alpha)

        known_beta = 0.8
        observed_beta = net_wcomps.beta
        self.assertEqual(observed_beta, known_beta)

        known_gamma = 0.3333333333333333
        observed_gamma = net_wcomps.gamma
        self.assertEqual(observed_gamma, known_gamma)

        known_eta = 2.75
        observed_eta = net_wcomps.eta
        self.assertEqual(observed_eta, known_eta)

    def test_lattice_network_wcomps_alpha(self):
        # with recorded components
        net_wcomps = tigernet.Network(s_data=self.lats.copy(), record_components=True)
        net_wcomps.calc_net_stats(conn_stat="alpha")

        known_alpha = 0.0
        observed_alpha = net_wcomps.alpha
        self.assertEqual(observed_alpha, known_alpha)

    def test_lattice_network_wcomps_beta(self):
        # with recorded components
        net_wcomps = tigernet.Network(s_data=self.lats.copy(), record_components=True)
        net_wcomps.calc_net_stats(conn_stat="beta")

        known_beta = 0.8
        observed_beta = net_wcomps.beta
        self.assertEqual(observed_beta, known_beta)

    def test_lattice_network_wcomps_gamma(self):
        # with recorded components
        net_wcomps = tigernet.Network(s_data=self.lats.copy(), record_components=True)
        net_wcomps.calc_net_stats(conn_stat="gamma")

        known_gamma = 0.3333333333333333
        observed_gamma = net_wcomps.gamma
        self.assertEqual(observed_gamma, known_gamma)

    def test_lattice_network_wcomps_eta(self):
        # with recorded components
        net_wcomps = tigernet.Network(s_data=self.lats.copy(), record_components=True)
        net_wcomps.calc_net_stats(conn_stat="eta")

        known_eta = 2.75
        observed_eta = net_wcomps.eta
        self.assertEqual(observed_eta, known_eta)


class TestNeworkEntropyLattice1x1(unittest.TestCase):
    def setUp(self):
        self.lat = tigernet.generate_lattice(n_hori_lines=1, n_vert_lines=1)

    def test_lattice_network_entropy_xvariation(self):
        net = tigernet.Network(s_data=self.lat.copy())
        net.calc_entropy("MTFCC", "s_data")

        known_entropies = {"S1400": 0.0}
        observed_entropies = net.mtfcc_entropies
        self.assertEqual(observed_entropies, known_entropies)

        known_entropy = -0.0
        observed_entropy = net.network_mtfcc_entropy
        self.assertEqual(observed_entropy, known_entropy)

    def test_lattice_network_entropy_wvariation(self):
        _lat = self.lat.copy()
        _lat["MTFCC"] = ["S1100", "S1200", "S1400", "S1700"]
        net = tigernet.Network(s_data=_lat)
        net.calc_entropy("MTFCC", "s_data")

        known_entropies = {"S1100": -0.5, "S1200": -0.5, "S1400": -0.5, "S1700": -0.5}
        observed_entropies = net.mtfcc_entropies
        self.assertEqual(observed_entropies, known_entropies)

        known_entropy = 2.0
        observed_entropy = net.network_mtfcc_entropy
        self.assertEqual(observed_entropy, known_entropy)


##########################################################################################
# Empirical testing
##########################################################################################


class TestNeworkStatsEmpirical(unittest.TestCase):
    def setUp(self):

        # set up the network instantiation parameters
        discard_segs = None
        kwargs = {"s_data": roads.copy(), "from_raw": True}
        attr_kws = {"attr1": ATTR1, "attr2": ATTR2}
        kwargs.update(attr_kws)
        comp_kws = {"record_components": True, "largest_component": True}
        kwargs.update(comp_kws)
        geom_kws = {"record_geom": True, "calc_len": True}
        kwargs.update(geom_kws)
        mtfcc_kws = {"discard_segs": discard_segs, "skip_restr": SKIP_RESTR}
        mtfcc_kws.update({"mtfcc_split": INTRST, "mtfcc_intrst": INTRST})
        mtfcc_kws.update({"mtfcc_split_grp": SPLIT_GRP, "mtfcc_ramp": RAMP})
        mtfcc_kws.update({"mtfcc_split_by": SPLIT_BY, "mtfcc_serv": SERV_DR})
        kwargs.update(mtfcc_kws)

        # full network
        self.network = tigernet.Network(**kwargs)
        self.network.calc_net_stats()

        # simplified network
        kws = {"record_components": True, "record_geom": True, "def_graph_elems": True}
        self.graph = self.network.simplify_network(**kws)
        self.graph.calc_net_stats()

    """
    def test_network_sinuosity(self):
        known_sinuosity = [1.0] * 10
        observed_sinuosity = list(self.network.s_data["sinuosity"])
        self.assertEqual(observed_sinuosity, known_sinuosity)

    def test_network_sinuosity_stats(self):
        known_max = 1.0
        observed_max = self.network.max_sinuosity
        self.assertEqual(observed_max, known_max)

        known_min = 1.0
        observed_min = self.network.min_sinuosity
        self.assertEqual(observed_min, known_min)

        known_mean = 1.0
        observed_mean = self.network.mean_sinuosity
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.0
        observed_std = self.network.std_sinuosity
        self.assertEqual(observed_std, known_std)

    def test_graph_sinuosity(self):
        known_sinuosity = [2.23606797749979, numpy.inf, 1.0]
        observed_sinuosity = list(self.graph.s_data["sinuosity"])
        self.assertEqual(observed_sinuosity, known_sinuosity)

    def test_graph_sinuosity_stats(self):
        known_max = 2.23606797749979
        observed_max = self.graph.max_sinuosity
        self.assertEqual(observed_max, known_max)

        known_min = 1.0
        observed_min = self.graph.min_sinuosity
        self.assertEqual(observed_min, known_min)

        known_mean = 1.8240453183331933
        observed_mean = self.graph.mean_sinuosity
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.71364417954618
        observed_std = self.graph.std_sinuosity
        self.assertEqual(observed_std, known_std)

    def test_network_node_degree_stats(self):
        known_max = 4
        observed_max = self.network.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.network.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 2.0
        observed_mean = self.network.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.816496580927726
        observed_std = self.network.std_node_degree
        self.assertEqual(observed_std, known_std)

    def test_graph_node_degree_stats(self):
        known_max = 4
        observed_max = self.graph.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.graph.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 2.0
        observed_mean = self.graph.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 1.7320508075688772
        observed_std = self.graph.std_node_degree
        self.assertEqual(observed_std, known_std)
    """

    """
    def test_network_node_degree_stats(self):
        known_max = 2
        observed_max = self.network.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.network.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 1.3333333333333333
        observed_mean = self.network.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.5163977794943223
        observed_std = self.network.std_node_degree
        self.assertEqual(observed_std, known_std)

    def test_graph_node_degree_stats(self):
        known_max = 1
        observed_max = self.graph.max_node_degree
        self.assertEqual(observed_max, known_max)

        known_min = 1
        observed_min = self.graph.min_node_degree
        self.assertEqual(observed_min, known_min)

        known_mean = 1.0
        observed_mean = self.graph.mean_node_degree
        self.assertEqual(observed_mean, known_mean)

        known_std = 0.0
        observed_std = self.graph.std_node_degree
        self.assertEqual(observed_std, known_std)
    """


class TestNeworkConnectivityEmpirical(unittest.TestCase):
    def setUp(self):
        pass


class TestNeworkEntropyEmpirical(unittest.TestCase):
    def setUp(self):

        # set up the network instantiation parameters
        discard_segs = None
        kwargs = {"s_data": roads.copy(), "from_raw": True}
        attr_kws = {"attr1": ATTR1, "attr2": ATTR2}
        kwargs.update(attr_kws)
        comp_kws = {"record_components": True, "largest_component": True}
        kwargs.update(comp_kws)
        geom_kws = {"record_geom": True, "calc_len": True}
        kwargs.update(geom_kws)
        mtfcc_kws = {"discard_segs": discard_segs, "skip_restr": SKIP_RESTR}
        mtfcc_kws.update({"mtfcc_split": INTRST, "mtfcc_intrst": INTRST})
        mtfcc_kws.update({"mtfcc_split_grp": SPLIT_GRP, "mtfcc_ramp": RAMP})
        mtfcc_kws.update({"mtfcc_split_by": SPLIT_BY, "mtfcc_serv": SERV_DR})
        kwargs.update(mtfcc_kws)

        # full network
        self.network = tigernet.Network(**kwargs)
        self.network.calc_entropy("MTFCC", "s_data")

    def test_network_entropy_variation(self):

        known_entropies = {
            "S1630": -0.15869726894257252,
            "S1100": -0.08968927494169666,
            "S1400": -0.2700938933248304,
            "S1200": -0.42847006925102654,
        }
        observed_entropies = self.network.mtfcc_entropies
        for mtfcc_type, known_entropy_val in known_entropies.items():
            self.assertAlmostEqual(observed_entropies[mtfcc_type], known_entropy_val)

        known_entropy = 0.9469505064601262
        observed_entropy = self.network.network_mtfcc_entropy
        self.assertAlmostEqual(observed_entropy, known_entropy)


if __name__ == "__main__":
    unittest.main()
