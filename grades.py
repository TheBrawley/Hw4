def average_score(scores:list[int])->int:
    total = 0
    for score in scores:
        total += score
    return total / len(scores)
    
def pass_fail(score:int)->str:
    if score >= 60:
        return "Pass"
    else:
        return "Fail"
        
def analyze_scores(scores:list[int])->None:
    for scores in scores:
        print(f"score {scores} -> {pass_fail(scores)}")

if __name__ == "__main__":
    scores = [95, 82, 67, 54, 100, 73]

    print("All scores:", scores)
    print("Class average:", average_score(scores))
    print()

    analyze_scores(scores)