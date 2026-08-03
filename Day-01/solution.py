class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        extra = min((mainTank - 1) // 4, additionalTank)
        return (mainTank + extra) * 10
