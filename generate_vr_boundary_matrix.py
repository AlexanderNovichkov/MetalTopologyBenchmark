#!/usr/bin/env python

import argparse
import time

import gudhi
from gudhi.rips_complex import RipsComplex

import utils

parser = argparse.ArgumentParser(
)
parser.add_argument("-p", "--pointcloud_name", type=str, required=True)
parser.add_argument("-e", "--max_edge_length", type=float, default=100000)
parser.add_argument("-d", "--max_dimension", type=int, default=2)

args = parser.parse_args()

file = f'datasets/pointclouds/{args.pointcloud_name}.off'

with open(file) as f:
    first_line = f.readline()
    if (first_line == "OFF\n") or (first_line == "nOFF\n"):
        print("Reading points from OFF file")
        point_cloud = gudhi.read_points_from_off_file(off_file=file)

        print("Creating rips_complex with max_edge_length =", args.max_edge_length)
        rips_complex = RipsComplex(
            points=point_cloud, max_edge_length=args.max_edge_length
        )

        print("Creating simplex_tree with max_dimension=", args.max_dimension)
        simplex_tree = rips_complex.create_simplex_tree(
            max_dimension=args.max_dimension
        )

        print("Number of simplices =" + repr(simplex_tree.num_simplices()))

        print("Making boundary matrix...")
        boundary_matrix = utils.make_boundary_matrix(simplex_tree)

        print("Writing boundary matrix in metal format...")
        utils.write_boundary_matrix_with_metal_format(
            f'datasets/vr_boundary_matrices/{args.pointcloud_name}_'
            f'{args.max_dimension}_{args.max_edge_length}_metal.txt',
            boundary_matrix)

        print("Writing boundary matrix in phat format...")
        utils.write_boundary_matrix_with_phat_format(
            f'datasets/vr_boundary_matrices/{args.pointcloud_name}_'
            f'{args.max_dimension}_{args.max_edge_length}_phat.txt',
            boundary_matrix)
