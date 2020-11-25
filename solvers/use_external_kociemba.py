import kociemba


def kociemba_to_ours(k_solve):
    k_to_ours = {"U": "B", "B": "D", "D": "F", "F": "U"}
    solve = ""
    for letter in k_solve:
        if letter in k_to_ours.keys():
            solve += k_to_ours[letter]
        else:
            solve += letter
    return solve


def external_kociemba(cube):
    if cube.get_matrix()[0, 0] == "g":
        return kociemba_to_ours(kociemba.solve(cube.get_cubestring(how="colorsURFDLB_g0")))
    else:
        cube.change(to="g")
        solution = kociemba_to_ours(kociemba.solve(cube.get_cubestring(how="colorsURFDLB_g0")))
        cube.change(to="w")
        return solution
