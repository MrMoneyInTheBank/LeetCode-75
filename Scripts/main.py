import os 
import shutil

def main():
    blind75_path = "/Users/anshumansingh/Desktop/Programming/LeetCode/Blind75"

    # Gather the paths for each topic
    topics = [d for d in os.listdir(blind75_path) if os.path.isdir(os.path.join(blind75_path, d))]

    # Gather subfolders
    topic_subfolders = {}
    for topic in topics:
        topic_path = os.path.join(blind75_path, topic)
        difficulties = [d for d in os.listdir(topic_path) if os.path.isdir(os.path.join(topic_path, d))]
        topic_subfolders[topic] = difficulties

    # Create folder for python
    for topic, difficulties in topic_subfolders.items():
        for difficulty in difficulties:
            python_folder_path = os.path.join(blind75_path, topic, difficulty, "Python")
            if not os.path.exists(python_folder_path):
                os.makedirs(python_folder_path)

    # Transfer files
    for topic, difficulties in topic_subfolders.items():
        for difficulty in difficulties:
            difficulty_folder_path = os.path.join(blind75_path, topic, difficulty)
            python_folder_path = os.path.join(difficulty_folder_path, "Python")

            py_files = [f for f in os.listdir(difficulty_folder_path) if f.endswith('.py')]

            for py_file in py_files:
                source_path = os.path.join(difficulty_folder_path, py_file)
                dest_path = os.path.join(python_folder_path, py_file)
                shutil.move(source_path, dest_path)
    
if __name__ == "__main__":
    main()
