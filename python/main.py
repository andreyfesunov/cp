import pyleet


def run_problem(problem_id, module):
    testcases = pyleet.get_testcase(problem_id=problem_id)
    results = pyleet.run(testcases, solution_path=module)
    pyleet.print_results(results)


if __name__ == "__main__":
    import os

    module_path = "./leetcode"

    def get_max_module_number():
        submodules = []
        for filename in os.listdir(module_path):
            if filename.endswith(".py"):
                name = filename[:-3]
                if name.isdigit():
                    submodules.append(int(name))
        return max(submodules) if submodules else 0

    max_module_number = get_max_module_number()

    problem_id = input(f"problem_id: ({max_module_number})") or max_module_number

    run_problem(problem_id, f"{module_path}/{problem_id}.py")
