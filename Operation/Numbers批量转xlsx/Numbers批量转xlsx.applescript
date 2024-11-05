use scripting additions

on run {input, parameters}
	set theFolder to choose folder
	
	tell application "Finder"
		set theDocs to (every item in folder theFolder whose name extension is "Numbers") as alias list
		if (count of theDocs) = 0 then return
		
		repeat with aDoc in theDocs
			
			set docName to aDoc's name
			set exportName to (theFolder as text) & docName
			set exportName to exportName's text 1 thru -9 & ".xlsx"
			
			tell application "Numbers"
				open aDoc
				repeat while not (exists document 1)
				end repeat
				with timeout of 1200 seconds
					export front document to file exportName as Microsoft Excel
				end timeout
				-- close front document saving no
			end tell
			
			if (exists exportName as alias) then
				set extension hidden of (exportName as alias) to false
			end if
			
		end repeat
	end tell
	return input
end run