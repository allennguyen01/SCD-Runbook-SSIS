from getBatchJobGroups import getBatchJobGroups
from getFileTriggers import getFileTriggers
from getPathNames import getPathNames
from getScheduledPlans import getScheduledPlans
from getSchedules import getSchedules
from getVariables import getVariables

def main(): 
    getPathNames('xml\PROD_20221004.xml', 'csv\Path_Names.csv')
    getSchedules('xml\PROD_20221004.xml', 'csv\Schedules.csv')
    getBatchJobGroups('xml\PROD_20221004.xml', 'csv\Path_Names.csv', 'csv\Batch_Job_Groups.csv')
    getFileTriggers('xml\PROD_20221004.xml', 'csv\File_Triggers.csv')
    getScheduledPlans('xml\PROD_20221004.xml', 'csv\Schedules.csv', 'csv\Scheduled_Plans.csv')
    getVariables('xml\PROD_20221004.xml', 'csv\Variables.csv')

if __name__ == "__main__":
    main()
