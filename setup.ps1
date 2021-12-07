# Install Nuget
Register-PackageSource -Name Nuget -Location "http://www.nuget.org/api/v2" -ProviderName Nuget -Trusted

# Install the latest version of Python without admin privileges
find-package python | install-package -Scope CurrentUser

# find the path of Python installation
get-package python | % source

# You need to add manually the package executable path to your USER PATH.
# To get the current USER Path
[System.Environment]::GetEnvironmentVariable('Path', 'User')

# To set the current USER Path
[System.Environment]::SetEnvironmentVariable('Path', $newPathInSingleStringSeparatedByColumn, 'User')