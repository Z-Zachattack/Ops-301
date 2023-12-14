# Script Name:                  Ops301d10 - Class 13
# Author:                       Zachariah Woodbridge
# Date of latest revision:      13 Dec 2023
# Purpose:                      Powershell Active Directory

# Import the Active Directory module
Import-Module ActiveDirectory

# Main
New-ADUser -Name "Franz Ferdinand" -Department "TPS Department" -Title "TPS Reporting lead" -Company "Globex USA" -City "Springfield" -State "Oregon" -EmailAddress "ferdi@GlobeXpower.com"
# End
