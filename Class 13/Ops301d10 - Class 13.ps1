# Script Name:                  Ops301d10 - Class 13
# Author:                       Zachariah Woodbridge
# Date of latest revision:      13 Dec 2023
# Purpose:                      Powershell AD Automation Overview

# Import the Active Directory module
Import-Module ActiveDirectory


# Declaration of variables

# Prompt for user details
$firstName = "Franz"
$lastName = "Ferdinand"
$title = "TPS Reporting Lead"
$department = "TPS"
$company = "GlobeX USA"
$location = "Springfield OR"

# Build email address
$emailAddress = "$firstName@GlobeXpower.com"

# Build UPN logon
$upn = "$firstName@GlobeXpower.com"

# Build organizational unit path
$ouPath = "OU=$department,OU=GlobeX USA,DC=GlobeXpower,DC=com"


# Main
# Create new user
New-ADUser -Name "$firstName $lastName" -SamAccountName "$firstName$lastName" -Title $title -Department $department -Company $company -EmailAddress $emailAddress -UserPrincipalName $upn -Path $ouPath -Description "$firstName $lastName is the $title at $company in $location office." -PasswordNeverExpires:$true

# Optional: Display confirmation message
Write-Host "User $firstName $lastName created successfully!"
# End
