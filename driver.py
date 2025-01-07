import os

def run_script(script_path, args=None):
    command = f'python3 {script_path}'
    if args:
        command += ' ' + ' '.join(args)
    try:
        os.system(command)
    except Exception as e:
        print(f"An error occurred while running {script_path}: {e}")

def main():
    try:
        print("Choose an option to run:")
        print("Section 1. Candidate experience data")
        print("Section 2. Candidate filter based selection")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            print("Fetching candidate experience\n")
            run_script('candidate_data/main_data.py')
        elif choice == '2':
            print("Enter the following details to filter candidates or hit enter to skip filter:")
            industry = input("Enter industry (in quotes): ")
            min_exp = input("Enter minimum years of experience: ")
            skills = input("Enter skills (in quotes and space-separated): ")
            filter_options = []
            if industry:
                filter_options.extend(['--industry', industry])
            if skills:
                filter_options.extend(['--skills', skills])
            if min_exp:
                filter_options.extend(['--min_exp', min_exp])

            print("Filtering information and storing into DB\n")
            run_script('candidate_filter/main_filter.py', filter_options)
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()