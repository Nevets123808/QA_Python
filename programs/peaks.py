def planner(heights):
    if len(heights)<=1:
        return heights
    options = [[peak for peak in heights[index+1:] if peak>heights[index]] for index in range(len(heights))]
    numOptions = [len(option) for option in options]
    choice = numOptions.index(max(numOptions))
    return [heights[choice]]+planner(options[choice])
peaks = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(planner(peaks))