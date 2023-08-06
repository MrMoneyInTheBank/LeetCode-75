import os 
import sys 

def main():
    if len(sys.argv) < 2:
        print("Please provide a language name as a command-line argument.")
        return 
    
    language = sys.argv[1]
    blind75_path = "/Users/anshumansingh/Desktop/LeetCode/Blind75"
    
    # Gather the paths for each topic
    topics = [d for d in os.listdir(blind75_path) if os.path.isdir(os.path.join(blind75_path, d))]

    # Navigate through folder structure
    for topic in topics:
        topic_path = os.path.join(blind75_path, topic)
        difficulties = [d for d in os.listdir(topic_path) if os.path.isdir(os.path.join(topic_path, d))]
    
        for difficulty in difficulties:
            language_folder_path = os.path.join(blind75_path, topic, difficulty, language)
            if not os.path.exists(language_folder_path):
                os.makedirs(language_folder_path)

if __name__ == "__main__":
    main()
