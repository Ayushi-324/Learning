class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:  #single pass loop
            id_part, content_part = log.split(" ", 1)  #split id and content

            if content_part[0].isdigit(): #if its no add bina change 
                digit_logs.append(log)
            else:
                letter_logs.append((content_part, id_part, log)) # ()add data in tuple for multi level sort ex - ("content", "id", "fulllog") 

        letter_logs.sort(key=lambda x: (x[0], x[1])) #step A: compare[0] content uske hisab se sort else if a tie b step: compare x[1] id 

        sorted_letters = [item[2] for item in letter_logs] #stores final clean string and item holds full tuple

        return sorted_letters + digit_logs
