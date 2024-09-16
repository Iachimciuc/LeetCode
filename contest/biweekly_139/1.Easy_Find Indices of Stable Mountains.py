class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable_indices = []
        n = len(height)

        for i in range(1, n):
            if height[i - 1] > threshold:
                stable_indices.append(i)

        return stable_indices