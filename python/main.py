import pyleet


def run_problem(problem_id, module):
    testcases = pyleet.get_testcase(problem_id=problem_id)
    results = pyleet.run(testcases, solution_path=module)
    pyleet.print_results(results)


if __name__ == "__main__":
    problem_id = input("problem_id: ")

    run_problem(problem_id, f"./leetcode/{problem_id}.py")
