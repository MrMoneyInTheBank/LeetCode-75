from typing import List 

class Solution:
	def alienOrder(self, words: List[str]) -> str:
		graph = {char: set() for word in words for char in word}
                
		for i in range(len(words) - 1):
			word1, word2 = words[i], words[i+1]
			shorter = min(len(word1), len(word2))

			if len(word1) > len(word2) and word1[:shorter] == word2[:shorter]:
				return ""
			
			for j in range(shorter):
				if word1[j] != word2[j]:
					graph[word1[j]].add(word2[j])
					break
			
		res = []
		seen = {}

		def dfs(char):
			if char in seen:
				return seen[char]
		
			seen[char] = True
			for child in graph[char]:
				if dfs(child):
					return True
			seen[char] = False 
			res.append(char)
		
		for char in graph:
			if dfs(char):
				return ""
		
		return "".join(res[::-1])