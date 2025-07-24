import pyleet


def run_problem(problem_id, method, module):
    testcases = pyleet.get_testcase(problem_id=problem_id)
    results = pyleet.run(testcases, method=method, solution_path=module)
    pyleet.print_results(results)


if __name__ == "__main__":
    problem_id = input("problem_id: ")

    run_problem(problem_id, "run", f"./leetcode/{problem_id}.py")
