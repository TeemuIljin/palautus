import unittest

from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        self.assertEqual(self.stats.search("Gretzky").name, "Gretzky")

    def test_search_returns_none_when_not_found(self):
        self.assertIsNone(self.stats.search("Nonexistent"))

    def test_team_returns_players_of_team(self):
        edm = self.stats.team("EDM")
        self.assertEqual(len(edm), 3)
        self.assertTrue(all(p.team == "EDM" for p in edm))

    def test_top_returns_n_plus_one_players(self):
        top3 = self.stats.top(3)
        self.assertEqual(len(top3), 4)
        self.assertGreaterEqual(top3[0].points, top3[1].points)

