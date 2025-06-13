import sys
import os
import random
'''
June 12, 2025
Terminal investment fv calculation script
'''
# put this on github later

'''
To run, type python3 for mac and python for windows into terminal, follwed by total path into terminal, 
and then the required starting investment argument 
'''

def show_help():
    print('''
    You can run this script from terminal arguments or with python inputs.
    To run it from the terminal, type anything for a second argument, such as "t". You will then be prompted to run the
    script again with arguments for an initial investment amount (integer), number of years (integer), and investment favorability:
    "good", "normal", or "poor".
    
    Running the script normally ('python3 calculate.py) you will be asked for the initial investment 
    the amount of years for the investment and
    the investment favorability of good, normal, or poor via input.  


    ''')
    sys.exit()

if len(sys.argv)>1 and ('?' in sys.argv or '--help' in sys.argv or '-h' in sys.argv):
    show_help()

def run_from_terminal():
    try:
        investment, years, favorability=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3].lower().strip()
        calculate_investment(investment,years,favorability)

    except(IndexError):
        print("Usage: python3 calculate.py <amount> <years> <favorability>")
        print("Example: python3 calculate.py 1000 5 good")
    except(ValueError):
        print('Enter the arguments formatted correctly')
        

def run_with_inputs():
    investment=int(input('Enter the initial investment amount: '))
    years=int(input('Enter the amount of years: '))
    favorability=input('Enter good, normal, or poor investment favorability: ').lower().strip()
    calculate_investment(investment,years,favorability)



def calculate_investment(investment, years, favorability):
    original_investment=investment

    print('\nCalculating investment outcome:\n')
    print(f'Starting with {investment} dollars')
    for i in range(1,years+1):
        if favorability in ['good, normal','poor']:
            if favorability=='good':
                rateofreturn=round(random.uniform(9,14),2)
            elif favorability=='normal':
                rateofreturn=round(random.uniform(6,11.5),2)
            elif favorability=='poor':
                rateofreturn=round(random.uniform(-1,5.5),2)
            formularate=1+rateofreturn/100
        else:
            raise ValueError('Enter the arguments formatted correctly')    

        print(f'Year {i}: {investment*formularate:.2f}')
        # string method here
        print(f'The investment returned {rateofreturn}% this year\n')
        # formatting:
        investment = round(investment * formularate, 2)
    print(f'\nThe investment grew by {investment-original_investment:.2f} dollars over {years} years\nResulting in a total growth of {((investment/original_investment)-1)*100:.2f}%')
    # formatting ftw
    rate=1.09
    # print('\nString formatting testing')
    # print(str(rate)[2:])
    # string methods are cool



currentdirectory=os.getcwd()
totalpath=os.path.join(currentdirectory, 'calculate.py')

print(f'\nTotal path is {totalpath}')
# runscript for mac=
# python3 calculatescript.py
# runscript for windows=
# python calculatescript.py

def main():
    if len(sys.argv)==2 or len(sys.argv)==3 :
        print('Run again from terminal with these full arguments:')
        print('Usage: python3 calculate.py <amount> <years> <favorability>')
    elif(len(sys.argv))==1:
        run_with_inputs()
        print('\n\nYou can also run from the terminal, enter arguments like this:')
        print('python3 calculate.py <amount> <years> <favorability>')

    elif len(sys.argv) > 3:
        run_from_terminal()
if __name__=='__main__':
    main()