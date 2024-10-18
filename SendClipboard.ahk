#Requires AutoHotkey v2.0

^k::
{
    KeyWait "Control"
    SetKeyDelay 20, 20
    ; SendText A_Clipboard
    ; SendInput A_Clipboard
    SendEvent A_Clipboard
}