# -*- coding: utf-8 -*-


class MechCreator(object):
    """
    A tool for creating a custom battlemech for the Battletech games
    """

    def __init__(self):
        """
        object initialization
        """
        # holds the values for all the engines {engine weight: [engine rating]}
        self.engines = {
            0.5: [10, 15, 20, 25],
            1.0: [30, 35, 40, 45],
            1.5: [50, 55],
            2.0: [65, 70, 75],
            2.5: [80, 85],
            3.0: [90, 95, 100],
            3.5: [105, 110],
            4.0: [115, 120, 125],
            4.5: [130, 135],
            5.0: [140, 145],
            5.5: [150, 155],
            6.0: [160, 165, 170],
            7.0: [175, 180],
            7.5: [185, 190],
            8.0: [195],
            8.5: [200, 205],
            9.0: [210],
            9.5: [215],
            10.0: [220, 225],
            10.5: [230],
            11.0: [235],
            11.5: [240],
            12.0: [245],
            12.5: [250],
            13.0: [255],
            13.5: [260],
            14.0: [265],
            14.5: [270],
            15.5: [275],
            16.0: [280],
            16.5: [285],
            17.5: [290],
            18.0: [295],
            19.0: [300],
            19.5: [305],
            20.5: [310],
            21.5: [315],
            22.5: [320],
            23.5: [325],
            24.5: [330],
            25.5: [335],
            27.0: [340],
            28.5: [345],
            29.5: [350],
            31.5: [355],
            33.0: [360],
            34.5: [365],
            36.5: [370],
            38.5: [375],
            41.0: [380],
            43.5: [385],
            46.0: [390],
            49.0: [395],
            52.5: [400]}
        # defines the internal structure based on the mech tonnage
        self.internal_structure_table = {
            10: {
                'centre_torso': 4, 'torso_sides': 3, 'arms': 1, 'legs': 2},
            15: {
                'centre_torso': 5, 'torso_sides': 4, 'arms': 2, 'legs': 3},
            20: {
                'centre_torso': 6, 'torso_sides': 5, 'arms': 3, 'legs': 4},
            25: {
                'centre_torso': 8, 'torso_sides': 6, 'arms': 4, 'legs': 6},
            30: {
                'centre_torso': 10, 'torso_sides': 7, 'arms': 5, 'legs': 7},
            35: {
                'centre_torso': 11, 'torso_sides': 8, 'arms': 6, 'legs': 8},
            40: {
                'centre_torso': 12, 'torso_sides': 10, 'arms': 6, 'legs': 10},
            45: {
                'centre_torso': 14, 'torso_sides': 11, 'arms': 7, 'legs': 11},
            50: {
                'centre_torso': 16, 'torso_sides': 12, 'arms': 8, 'legs': 12},
            55: {
                'centre_torso': 18, 'torso_sides': 13, 'arms': 9, 'legs': 13},
            60: {
                'centre_torso': 20, 'torso_sides': 14, 'arms': 10, 'legs': 15},
            65: {
                'centre_torso': 21, 'torso_sides': 15, 'arms': 10, 'legs': 14},
            70: {
                'centre_torso': 22, 'torso_sides': 15, 'arms': 11, 'legs': 15},
            75: {
                'centre_torso': 23, 'torso_sides': 16, 'arms': 12, 'legs': 16},
            80: {
                'centre_torso': 25, 'torso_sides': 17, 'arms': 13, 'legs': 17},
            85: {
                'centre_torso': 27, 'torso_sides': 18, 'arms': 14, 'legs': 18},
            90: {
                'centre_torso': 29, 'torso_sides': 19, 'arms': 15, 'legs': 19},
            95: {
                'centre_torso': 30, 'torso_sides': 20, 'arms': 16, 'legs': 20},
            100: {
                'centre_torso': 31, 'torso_sides': 21, 'arms': 17, 'legs': 21}}


class Mech(object):
    """
    A class for storing the info for a custom battlemech
    """

    def __init__(self):
        """
        object initialization
        """
        # stores the mech tonnage
        self.tonnage = None
        # stores the mech engine rating
        self.engine_rating = None
        # saves the internal structure based on the table
        self.internal_structure = {
            'centre_torso': None,
            'torso_sides': None,
            'arms': None,
            'legs': None}
        # saves the movement points
        self.movement_points = {
            'walking': None,
            'running': None,
            'jumping': None}
        self.heatsinks = 10
        self.armour_value = None
        self.critical_locations = {
            'head': 1,
            'centre_torso': 2,
            'torso_sides': 12,
            'arms': 8,
            'legs': 2}
        self.weapons = None
        self.ammo = None
