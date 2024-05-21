# Import commands
import os                           # Built - IN Modules
import sys                          # Built - IN Modules
import time                         # Built - IN Modules
from datetime import datetime       # Built - IN Modules

try:
    import MySQLdb as connector     #pip install MySQLdb
except:
    print("MySQLdb Not Installed")
    print("Installing MySQLdb")
    os.system("pip3 install MySQLdb")
    import MySQLdb as connector

try:
    from pandas import *
except:
    print("Installing Pandas....")
    os.system("pip3 install pandas")
    from pandas import *

try:
    from matplotlib import pyplot as plt
except:
    print("Installing Matplotlib....")
    os.system("pip3 install matplotlib")
    from matplotlib import pyplot as plt

try:
    from rich.console import Console
    from rich.markdown import Markdown
except:
    print("Installing Rich module....")
    os.system("pip3 install rich")
    try:
        from rich.console import Console
        from rich.markdown import Markdown
    except:
        print("Rich Can't be installed for some reason...")
        pass
try:
    console = Console()
except:
    pass

# Rich Styling
style = "cyan"
style1 = "yellow"
style2 = "magenta"

class main():
    # FUNCTIONS

    def p(x,style):           #Rich Handling if not installed properly
        try:
            console.print(x,style=style)
        except:
            print(x)

    def printer():      # Main Printer(Initial)
        try:
            console.print(Markdown("# The Analyser"))
            console.print("[bold] Talk is Cheap, Show me the Code[/bold] -- Linus Torvalds".center(130),style="yellow")
        except:
            print("Welcome To The Analyser.....")
        main.p("1. Analyse Different Crimes in India.\n2. Analyse Murders.","cyan")
        main.p("3. Visualise Crimes\n4. Visualise Murders\n5. Entry Of Data To Database\n6. Exit\n","cyan")

    def printer_8_9():    #crime printer of option 8 and 9
        main.p("1. Total number of crimes in particular age group.",style)
        main.p("2. Total number of crimes in particular age group in a given state.",style)
        main.p("3. Total number of crimes in particular age group in a given state in a given year.",style)

    def crime_printer():   # Main Crime printer(All options)
        main.p("What do you want to do with data?",style=style)
        main.p("1. Total Number of crimes in India from 2001 to 2012.",style=style)
        main.p("2. Total Number of crimes in particular State.",style=style)
        main.p("3. Total Number of crimes in particular year.",style=style)
        main.p("4. Total Number of crimes in a state in particular year.",style=style)   
        main.p("5. Particular Crime in the given year.",style=style)
        main.p("6. Particular Crime in the given State.",style=style)
        main.p("7. Particular Crime in the given State in given Year.",style=style)
        main.p("8. Analyse Crimes on Male(with Age group).",style=style)
        main.p("9. Analyse Crimes on Female(with age group)",style=style)
        main.p("10. Exit",style=style)

    def murder_printer():   #Murder printer Main (All options)
        main.p("What do you want to do with data?\n",style=style)
        main.p("1. Total Number of Murders in India from 2013",style=style)
        main.p("2. Total Number of Murders in particular State.",style=style) 
        main.p("3. Murder of a Female(with Age group).",style=style)
        main.p("4. Murder of a Male(with age group)",style=style)
        main.p("5. Murder of a Female(with Age group) in specific state.",style=style)
        main.p("6. Murder of a male(with Age group) in specific state.",style=style)
        main.p("7. Exit",style)

    def murder_m_f(gen):
        if gen == "female":
            #Murder of female in a state with specific age group also.
                    df = murder.loc[1:len(murder.index)+1:3,['STATE/UT','Upto 10 years','10-15 years','15-18 years','18-30 years','30-50 years','Above 50 years']]
        elif gen == "male":
            #Murder of male in a state with specific age group also.
            df = murder.loc[0:len(murder.index)+1:3,['STATE/UT','Upto 10 years','10-15 years','15-18 years','18-30 years','30-50 years','Above 50 years']]
        list1 = []
        list_states = []
        dict1 ={}
        dict2 = {}
        sum = 0
        for index,cols in df.iteritems():
            if index == 'STATE/UT':
                for i in cols:
                    list_states.append(i)
            list1.append(index)
        list1.remove('STATE/UT')
        for index,value in enumerate(list1):
            main.p(f"{index+1}. {value}",style=style1)
            dict1[index+1] = value
        inp3 = int(input("Enter Your Choice :"))
        for index,value in enumerate(list_states):
            main.p(f"{index+1}. {value}",style=style1)
            dict2[index+1] = value
        inp4 = int(input("Enter Your Choice :"))
        df1 = df.loc[:,['STATE/UT',dict1[inp3]]]
        for index,row in df1.iterrows():
            if row[0] == dict2[inp4]:
                sum = row[1]
        print()
        main.p(f"Your Result :{sum}",style=style2)
        print()

    def m_f1(gen):   #Male female choice 1
        df = crimes.loc[13:len(crimes.index)+1:14,[f'{gen} upto 10 years',f'{gen} 10-15 years',f'{gen} 15-18 years',f'{gen} 18-30 years',f'{gen} 30-50 years',f'{gen} above 50 years']]
        list1 = []
        dict1 = {}
        sum = 0
        for index,cols in df.iteritems():
            list1.append(index)
        for index,values in enumerate(list1):
            main.p(f"{index+1}. {values}",style=style1)
            dict1[index+1] = values
        inp4 = int(input("Enter Your Choice :"))
        for index,cols in df.iteritems():
            if index == dict1[inp4]:
                cols.index = range(len(df.index))
                for i in range(len(df.index)):
                    sum+=cols[i]
        main.p(f"Total Number of crimes in {dict1[inp4]} = {sum}",style=style2)

    def m_f2(gen):  #Male female choice 2
        df = crimes.loc[13:len(crimes.index)+1:14,['STATE/UT',f'{gen} upto 10 years',f'{gen} 10-15 years',f'{gen} 15-18 years',f'{gen} 18-30 years',f'{gen} 30-50 years',f'{gen} above 50 years']]
        list1 = []
        dict1 = {}
        list2 = []
        dict_states = {}
        sum = 0
        for index,cols in df.iteritems():
            list1.append(index)
        list1.remove('STATE/UT')
        for index,values in enumerate(list1):
            main.p(f"{index+1}. {values}",style=style1)
            dict1[index+1] = values
        inp4 = int(input("Enter Your Choice :"))
        for index,row in df.iterrows():
            if row[0] in list2:
                pass
            else:
                list2.append(row[0])
        for index,values in enumerate(list2):
            main.p(f"{index+1}. {values}",style=style1)
            dict_states[index+1] = values
        inp5 = int(input("Enter The State :"))
        df1 = df.loc[:,['STATE/UT',dict1[inp4]]]
        for index,row in df1.iterrows():
            if row[0] == dict_states[inp5]:
                sum += row[1]
        main.p(f"Your Result :{sum} ",style=style2)

    def m_f3(gen):   #Male female choice 3
        df = crimes.loc[13:len(crimes.index)+1:14,['STATE/UT','YEAR',f'{gen} upto 10 years',f'{gen} 10-15 years',f'{gen} 15-18 years',f'{gen} 18-30 years',f'{gen} 30-50 years',f'{gen} above 50 years']]
        list1 = []
        dict1 = {}
        list2 = []
        dict_states = {}
        sum = 0
        for index,cols in df.iteritems():
            list1.append(index)
        list1.remove('STATE/UT')
        list1.remove('YEAR')
        for index,values in enumerate(list1):
            main.p(f"{index+1}. {values}",style=style1)
            dict1[index+1] = values
        inp4 = int(input("Enter Your Choice :"))
        for index,row in df.iterrows():
            if row[0] in list2:
                pass
            else:
                list2.append(row[0])
        for index,values in enumerate(list2):
            main.p(f"{index+1}. {values}",style=style1)
            dict_states[index+1] = values
        inp5 = int(input("Enter The State :"))
        inp6 = int(input("Enter The Year [2001 - 2012] :"))
        df1 = df.loc[:,['STATE/UT','YEAR',dict1[inp4]]]
        for index,row in df1.iterrows():
            if row[0] == dict_states[inp5] and row[1] == inp6:
                sum += row[2]
        print()
        console.print(f"Your Result : {sum}",style=style2)
        print()

    def murder_finder_age_group(start,gender):
        murder_sample = read_csv("murder.csv",usecols=['Upto 10 years','10-15 years','15-18 years','18-30 years','30-50 years','Above 50 years'])
        murder_sample = murder_sample.loc[start:len(murder_sample.index)+1:3]
        list1 = murder_sample.T.index
        dict1 ={}
        sum = 0
        for index,values in enumerate(list1):
            main.p(f"{index+1}. {values}",style=style1)
            dict1[index+1] = values
        inp3 = int(input("Enter Your Choice :"))
        murder_sample.index = range(0,len(murder_sample.index))
        for i in range(0,len(murder_sample.index)):
            sum += murder_sample[dict1[inp3]][i]
        main.p()
        main.p(f"Total Number of {gender} murders = {sum}",style=style2)
        main.p()

    def crime_1():
        df = crimes.loc[13:len(crimes.index)+1:14,['Grand Total']]
        df.index = range(1,len(df.index)+1)
        total = 0
        for i in range(len(df.index)):
            total += df['Grand Total'][i+1]
        console.print()
        console.print("Total number of Crimes in India =",total,style=style2)
        console.print()

    def crime_2():
        df = crimes.loc[13:len(crimes.index)+1:14,['STATE/UT','YEAR','Grand Total']]
        df.index = range(1,len(df.index)+1)
        df_states = crimes.loc[13:len(crimes.index)+1:167,['STATE/UT']]
        df_states.index = range(1,len(df_states.index)+1)
        state_names = []
        dict1 ={}
        for i in range(len(df_states.index)):
            state_names.append(df_states['STATE/UT'][i+1])
        for index,value in enumerate(state_names):
            console.print(f"{index+1}. {value}",style=style1)
            dict1[index+1] = value
        inp3 = int(input("Enter Your Choice :"))
        sum = 0
        for index,row in df.iterrows():
            if row[0] == dict1[inp3]:
                sum += row[2]
        console.print()
        console.print(f"Total number of crimes in {dict1[inp3]} = {sum}.",style=style2)
        console.print()

    def crime_3():
        try:
            inp3 = int(input("Enter The Year (2001 to 2012):"))
        except:
            console.print("Enter The Valid Year")
            inp3 = int(input("Enter The Year (2001 to 2012):"))
        sum = 0
        for index,row in crimes.iterrows():
            if row[1] == inp3:
                sum += row[18]
        console.print()
        console.print(f"Total Number of Crimes in {inp3} = {sum}",style=style2)
        console.print()

    def crime_4():
        try:
            inp3 = int(input("Enter The Year (2001 to 2012):"))
        except:
            console.print("Enter The Valid Year")
            inp3 = int(input("Enter The Year (2001 to 2012):"))
        df_states = crimes.loc[13:len(crimes.index)+1:167,['STATE/UT']]
        df_states.index = range(1,len(df_states.index)+1)
        state_names = []
        dict1 ={}
        for i in range(len(df_states.index)):
            state_names.append(df_states['STATE/UT'][i+1])
        for index,value in enumerate(state_names):
            console.print(f"{index+1}. {value}",style=style1)
            dict1[index+1] = value
        inp4 = int(input("Enter Your Choice :"))
        df = crimes.loc[13:len(crimes.index)+1:14,['STATE/UT','YEAR','Grand Total']]
        for index,row in df.iterrows():
            if row[0] == dict1[inp4] and row[1] == inp3:
                crime_number = row[2]
        console.print()
        console.print(f"Number of Crime cases in {dict1[inp4]} in {inp3} = {crime_number}",style=style2)
        console.print()

    def crime_5():
        list1 = []
        dict1 = {}
        sum = 0
        for index,row in crimes.iterrows():
            if row[2] in list1:
                pass
            else:
                if row[2] == "Total" or row[2] == "For unlawful activity":
                    pass
                else:
                    list1.append(row[2])
            
        for index,value in enumerate(list1):
            console.print(f"{index+1}. {value}",style=style1)
            dict1[index+1] = value
        try:
            inp3 = int(input("Enter Your Choice :"))
        except:
            console.print("Your Choice should be in Integer!!")
            inp3 = int(input("Enter Your Choice :"))
        for index,row in crimes.iterrows():
            if row[2] == dict1[inp3]:
                sum += row[18]

        console.print(f"Total Number of Crimes = ",sum,style=style2)

    def crime_6():
        #Printing States
                    df_states = crimes.loc[13:len(crimes.index)+1:167,['STATE/UT']]
                    df_states.index = range(1,len(df_states.index)+1)
                    state_names = []
                    dict1 ={}
                    for i in range(len(df_states.index)):
                        state_names.append(df_states['STATE/UT'][i+1])
                    for index,value in enumerate(state_names):
                        console.print(f"{index+1}. {value}",style=style1)
                        dict1[index+1] = value
                    inp3 = int(input("Enter The place :"))
                    #Printing Crimes
                    list1 = []
                    dict2 = {}
                    sum = 0
                    for index,row in crimes.iterrows():
                        if row[2] in list1:
                            pass
                        else:
                            if row[2] == "Total" or row[2] == "For unlawful activity":
                                pass
                            else:
                                list1.append(row[2])
                    for index,value in enumerate(list1):
                        console.print(f"{index+1}. {value}",style=style1)
                        dict2[index+1] = value
                    inp4 = int(input("Enter The Kind :"))
                    for index,row in crimes.iterrows():
                        if row[0] == dict1[inp3] and row[2] == dict2[inp4]:
                            sum += row[18]
                    console.print()
                    console.print(f"Total Number of Crime {dict2[inp4]} in {dict1[inp3]} =",sum,style=style2)
                    console.print()

    def crime_7():
        try:
            inp3 = int(input("Enter The Year (2001 to 2012):"))
        except:
            console.print("Enter The Valid Year")
            inp3 = int(input("Enter The Year (2001 to 2012):"))
        #Printing States
        df_states = crimes.loc[13:len(crimes.index)+1:167,['STATE/UT']]
        df_states.index = range(1,len(df_states.index)+1)
        state_names = []
        dict1 ={}
        for i in range(len(df_states.index)):
            state_names.append(df_states['STATE/UT'][i+1])
        for index,value in enumerate(state_names):
            console.print(f"{index+1}. {value}",style=style1)
            dict1[index+1] = value
        inp4 = int(input("Enter The place :"))
        #Printing Crimes
        list1 = []
        dict2 = {}
        sum = 0
        for index,row in crimes.iterrows():
            if row[2] in list1:
                pass
            else:
                if row[2] == "Total" or row[2] == "For unlawful activity":
                    pass
                else:
                    list1.append(row[2])
        for index,value in enumerate(list1):
            console.print(f"{index+1}. {value}",style=style1)
            dict2[index+1] = value
        inp5 = int(input("Enter The Kind :"))
        for index,row in crimes.iterrows():
            if row[0] == dict1[inp4] and row[2] == dict2[inp5] and row[1] == inp3:
                sum += row[18]
        console.print()
        console.print(f"Total Number of Crime {dict2[inp5]} at {dict1[inp4]} in {inp3} =",sum,style=style2)
        console.print()

# Loader
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

# Loading Printer
def load(x):
    spinner = spinning_cursor()
    for _ in range(x):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
                
    

# --------------------------------------------------------------------------------------------------------

# CODE STARTS HERE
if __name__ == "__main__":
    #Printing Date
    console.print("Date -",datetime.date(datetime.now()),style=style2)
    console.print("Time -",datetime.time(datetime.now()),style=style2)
    console.print()

    #Printing Choice
    main.printer()        
    try:
        inp1 = int(input("Enter Your Choice :"))
    except:
        console.print("You need to enter your choice in Integer form.")
        inp1 = int(input("Enter Your Choice :"))
    if inp1 == 1:
        while True:
            crimes = read_csv("crimes.csv")
            main.crime_printer()
            try:
                inp2 = int(input("Enter Your Choice :"))
            except:
                console.print("You need to enter your choice in Integer form.")
                inp2 = int(input("Enter Your Choice :"))
        
            # Analysis Starts Here
            if inp2 == 1:
                main.crime_1()

            elif inp2 == 2:
                main.crime_2()

            elif inp2 == 3:
                main.crime_3()

            elif inp2 == 4:
                main.crime_4()
                
            elif inp2 == 5:
                main.crime_5()
                
            elif inp2 == 6:
                main.crime_6()
            
            elif inp2 == 7:
                main.crime_7()
            
            elif inp2 == 8:
                main.printer_8_9()
                inp3 = int(input("Enter Your choice :"))

                if inp3 == 1:
                    main.m_f1("Male")               
                elif inp3 == 2:
                    main.m_f2("Male")                    
                elif inp3 == 3:
                    main.m_f3("Male")
                else:
                    console.print("wrong choice!!")

            elif inp2 == 9:
                main.printer_8_9()
                inp3 = int(input("Enter Your Choice :"))

                if inp3 == 1:
                    main.m_f1("Female")
                elif inp3 == 2:
                    main.m_f2("Female")
                elif inp3 == 3:
                    main.m_f3("Female")
                else:
                    console.print("Terminating!!")
                    load(25)
                    exit()

            elif inp2 == 10:
                console.print("Please Wait\nTerminating")
                load(25)
                exit()
            
            else:
                console.print("Wrong Choice!!")
                break

            console.print("Do you want to continue? [y or n]")
            inp5 = input("Enter Your Choice :")

            if inp5 == ("y" or "Y"):
                continue
            else:
                console.print("Terminating!!")
                load(25)
                break


    elif inp1 == 2:
        murder = read_csv("murder.csv")
        while True:
            main.murder_printer()
            try:
                inp2 = int(input("Enter Your Choice :"))
            except:
                console.print("You need to enter your choice in Integer form.")
                inp2 = int(input("Enter Your Choice :"))
            
            if inp2 == 1:
                df = murder.loc[2:len(murder.index)+1:3,["Total"]]
                df.index = range(1,len(df.index)+1,1)
                sum = 0
                for index,row in df.iterrows():
                    sum += row[0]
                console.print("Total Number of Murders in 2013 =",sum)

            elif inp2 == 2:
                list1 = []
                dict1 = {}
                sum = 0
                for index,row in murder.iterrows():
                    if row[0] in list1:
                        pass
                    else:
                        list1.append(row[0])
                for index,value in enumerate(list1):
                    console.print(f"{index + 1}. {value}")
                    dict1[index+1] = value
                inp3 = int(input("Enter You Choice :"))
                for index,row in murder.iterrows():
                    if row[0] == dict1[inp3] and index in range(2,len(murder.index)+1,3):
                        sum += row[9]
                console.print(f"Total Number of Murders in {dict1[inp3]} =",sum)
            
            elif inp2 == 3:
                main.murder_finder_age_group(1,"Female")
            
            elif inp2 == 4:
                main.murder_finder_age_group(2,"Male")

            elif inp2 == 5:
                main.murder_m_f("female")

            elif inp2 == 6:
                main.murder_m_f("male")

            elif inp2 == 7:
                console.print("Please Wait while Terminating")
                load(25)
                exit()
            else:
                console.print("Wrong Choice \nTry Again")
                continue

            console.print("Do You want to continue? [y or n] :")
            inp3 = input("Enter :")
            if inp3 == ("y" or "Y"):
                continue
            else:
                console.print("Exiting The Analyser!!")
                load(30)
                break
    
    elif inp1 == 3:
        crimes = read_csv("crimes.csv")
        main.p("1. Line Graph\n2. Bar Graph",style1)
        inp2 = int(input("Enter Your Choice :"))

        if inp2 == 1:
            # plt.style.use('dark_background')
            crimes.plot(kind="line",ls=':',lw=0.5)
            plt.show()
        elif inp2 == 2:
            crimes = read_csv("crimes.csv",usecols=['STATE/UT','Grand Total'])
            # plt.style.use('dark_background')
            crimes.plot(kind="bar")
            plt.show()

    elif inp1 == 4:
        murders = read_csv("murder.csv")
        main.p("1. Line Graph\n2. Bar Graph",style1)
        inp2 = int(input("Enter Your Choice :"))

        if inp2 == 1:
            # plt.style.use('dark_background')
            murders.plot(kind="line",ls=':',lw=0.5)
            plt.show()
        elif inp2 == 2:
            murders = read_csv("murder.csv",usecols=['STATE/UT','Total'])
            plt.style.use('dark_background')
            murders.plot(kind="bar")
            plt.show()

    elif inp1 == 5:
        main.p("In order to Save Data into Mysql database you need to have a database first.\n",style)
        main.p("1.Create Database.\n2.Existing Database",style)
        inp100 = int(input("Enter Your Choice :"))

        inp1 = input("Enter The Name of the host :")
        inp2 = input("Enter The Name of the user :")
        inp4 = input("Enter The Password :")

        if inp100 == 1:
            conn = connector.connect(host=inp1,user=inp2,passwd=inp4)
            cur = conn.cursor()
            inp3 = input("Enter The Name of the database you want to create :")
            query = f"create database {inp3}"
            try:
                cur.execute(query)
                main.p("Database Created.",style="green")
            except:
                main.p("Database can't be created for some reason....",style1)
                main.p("Wrong Choice\nTerminating \nPlease Wait",style)  
                load(20)
                exit()
        elif inp100 == 2:
            pass
        
        if inp100 == 1:
            pass
        else:
            inp3 = input("Enter The Name of the Database already Created :")

        # Connecting Databse
        conn = connector.connect(host=inp1,user=inp2,passwd=inp4,db=inp3)
        cur = conn.cursor()

        if conn:
            console.print("\nDatabase successfully connected\n",style="green")
        else:
            console.print("Not Connected \nTerminating...\n",style="red")

        # LOGIC Starts
        query1 = "create table crimes(STATE_UT varchar(40),YEAR int,Pupose varchar(60),Total_No_of_cases_reported int,Male_upto_10_years int,Female_upto_10_years int,Male_10_15_years int,Female_10_15_years int,Male_15_18_years int,Female_15_18_years int,Male_18_30_years int,Female_18_30_years int,Male_30_50_years int,Female_30_50_years int,Male_above_50_years int,Female_above_50_years int,Total_Male int,Total_Female int,Grand_Total int);"

        query2 = "create table murder(STATE_UT varchar(40),YEAR int,GENDER varchar(20),Upto_10_years int,10_15_years int,15_18_years int,18_30_years int,30_50_years int,Above_50_years int,Total int)"

        try:
            cur.execute(query1)
        except:
            main.p("Table Crime can't be created or It has been already created.....",style)

        try:
            cur.execute(query2)
        except:
            main.p("Table Murder can't be created or It has been already created.....",style)

        crimes = read_csv('crimes.csv')
        murders = read_csv('murder.csv')

        print("\n1. Insert Data of crimes in INDIA.\n2. Insert Data of murders in INDIA.\n")
        inp200 = int(input("Enter Your Choice :"))
        main.p("THIS WILL TAKE SOME TIME\nTAKE REST...",style2)

        if inp200 == 1:
            for row in crimes.iterrows():
                query = f"insert into crimes values('{row[1][0]}',{row[1][1]},'{row[1][2]}',{row[1][3]},{row[1][4]},{row[1][5]},{row[1][6]},{row[1][7]},{row[1][8]},{row[1][9]},{row[1][10]},{row[1][11]},{row[1][12]},{row[1][13]},{row[1][14]},{row[1][15]},{row[1][16]},{row[1][17]},{row[1][18]});"
                try:
                    cur.execute(query)
                    conn.commit()
                except:
                    main.p("Values can't be Inserted\nTry Again Later...",style)
                    load(30)
                    exit()
        elif inp200 == 2:
            for row in murders.iterrows():
                query = f"insert into murder values('{row[1][0]}',{row[1][1]},'{row[1][2]}',{row[1][3]},{row[1][4]},{row[1][5]},{row[1][6]},{row[1][7]},{row[1][8]},{row[1][9]});"
                try:
                    cur.execute(query)
                    conn.commit()
                except:
                    main.p("Values can't be Inserted\nTry Again Later...",style)
                    load(30)
                    exit()
        else:
            main.p("WRONG CHOICE\nTERMINATING",style)
            load(25)
            exit()
        
    elif inp1 == 6:
        console.print("Terminating. Please Wait")
        load(25)
        exit()  

    else:
        console.print("Wrong Choice\nTerminating \nPlease Wait")  
        load(20)
        exit()        
else:
    pass