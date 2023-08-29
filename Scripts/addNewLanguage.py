import os 
import sys 
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Please provide a language name as a command-line argument.")
        return 
    
    language = sys.argv[1]
    blind75_path = "/Users/anshumansingh/Desktop/Programming/LeetCode/Blind75"
    
    # Gather the paths for each topic
    topics = [d for d in os.listdir(blind75_path) if os.path.isdir(os.path.join(blind75_path, d))]


    # Navigate through folder structure
    new_language_added = False
    for topic in topics:
        topic_path = os.path.join(blind75_path, topic)
        difficulties = [d for d in os.listdir(topic_path) if os.path.isdir(os.path.join(topic_path, d))]
    
        for difficulty in difficulties:
            language_folder_path = os.path.join(blind75_path, topic, difficulty, language)
            if not os.path.exists(language_folder_path):
                os.makedirs(language_folder_path)
                new_language_added = True
    
    # Create a new branch
    if new_language_added:
        subprocess.run(["git", "checkout", "-b", language])
        subprocess.run(["git", "add", "."])
        
        commit_message = f"{language} branch created"
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "push", "--set-upstream", "origin", language])

if __name__ == "__main__":
    main()
