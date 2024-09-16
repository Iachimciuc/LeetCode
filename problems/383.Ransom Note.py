class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        
        for char in ransomNoteCount:
            if ransomNoteCount[char] > magazineCount.get(char, 0):
                return False
        
        return True