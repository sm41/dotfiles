local mode = 0

local left  = "lavfi=[pan=stereo|FL=FL|FR=FL]"
local right = "lavfi=[pan=stereo|FL=FR|FR=FR]"

mp.add_key_binding("e", "dualmono-cycle", function()
    if mode == 0 then
        mp.commandv("af", "toggle", left)
        mp.osd_message("Left")
        mode = 1

    elseif mode == 1 then
        mp.commandv("af", "toggle", left)
        mp.commandv("af", "toggle", right)
        mp.osd_message("Right")
        mode = 2

    else
        mp.commandv("af", "toggle", right)
        mp.osd_message("Stereo")
        mode = 0
    end
end)