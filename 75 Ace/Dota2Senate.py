class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # convert the input string into a list for easier manipulation
        senate = list(senate)
        
        # create two deques to keep track of the indices of 'D' and 'R' senators
        d, r = deque(), deque()
        
        # populate the deques with the indices of 'D' and 'R' senators
        for i, ch in enumerate(senate):
            if ch == "R":
                r.append(i)
            else:
                d.append(i)

        # continue the elimination process until one party has no senators left
        while d and r:
            # remove the index of the next 'D' senator and 'R' senator
            dTurn = d.popleft()
            rTurn = r.popleft()

            #  if the 'R' senator's index is smaller than the 'D' senator's index,
            # add the index of the next 'D' senator at the end of the 'R' deque
            # else, add the index of the next 'R' senator at the end of the 'D' deque
            if rTurn < dTurn:
                r.append(dTurn + len(senate))
            else:
                d.append(rTurn + len(senate))
        
        # if there are senators remaining for the 'R' party, they win; otherwise, 'D' party wins
        if r:
            return "Radiant"
        else:
            return "Dire"
