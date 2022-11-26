class ATM:

    def __init__(self):
        self.hashmap = collections.defaultdict(lambda:0)
        
    def deposit(self, banknotesCount: List[int]) -> None:
        self.hashmap[20]  += banknotesCount[0]
        self.hashmap[50]  += banknotesCount[1]
        self.hashmap[100] += banknotesCount[2]
        self.hashmap[200] += banknotesCount[3]
        self.hashmap[500] += banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        used = []
        
        for note in [500, 200, 100, 50, 20]:
            if self.hashmap[note] >= 1:
                cnt = amount // note
                cnt_available = min(cnt, self.hashmap[note])
                self.hashmap[note] -= cnt_available
                amount -= (cnt_available * note)
                used.append(cnt_available)
            else:
                used.append(0)
        
        if amount == 0:
            return used[::-1]
        else:
            self.hashmap[20]  += used[4]
            self.hashmap[50]  += used[3]
            self.hashmap[100] += used[2]
            self.hashmap[200] += used[1]
            self.hashmap[500] += used[0]
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)