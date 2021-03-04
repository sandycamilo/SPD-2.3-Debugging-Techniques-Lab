# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

def good_level(total_cholostrol, ldl, triglyceride):
    return total_cholostrol < 200 and ldl < 100 and triglyceride < 150

def high_level(total_cholostrol, ldl, triglyceride):
    return 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200

def moderate_level(total_cholostrol, ldl, triglyceride):
    return 200 <total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200
    
def calculate_cholesterol_level():
    if good_level(total_cholostrol, ldl, triglyceride):
        print('*** Good level of cholestrol ***')
    elif high_level(total_cholostrol, ldl, triglyceride):
        print('*** High cholestrol level ***')
        print('start taking pills such as statins')
        print('start TLC diet')
    elif moderate_level(total_cholostrol, ldl, triglyceride):
        print('*** Borderline to moderately elevated ***')
        print("Start TLC diet")
        print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
        print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
        print('oats, barley, and other whole grains.')
        print('fruits such as apples, pears, bananas, and oranges.')
    else:
        print('Error: unhandled case.')

if __name__ == "__main__":
    total_cholostrol = 70
    ldl = 30
    triglyceride = 120
    good_level(total_cholostrol, ldl, triglyceride)
    high_level(total_cholostrol, ldl, triglyceride)
    moderate_level(total_cholostrol, ldl, triglyceride)
    calculate_cholesterol_level()

