from typing import List, Dict, Any, Union
import time
import pyautogui
import keyboard
import sys

def action(action_list: List[Dict[str, Any]]) -> Union[Dict[str, int], str, None]:
    """Do something to the computer in order
    Every item in the list is a dict, only dict in the following format are allowed
    {"type": "click", "x": int, "y": int}
    {"type": "mousedown"}
    {"type": "mouseup"}
    {"type": "mousemove", "x": int, "y": int}
    {"type": "scroll", "x": int, "y": int}
    {"type": "input", "text": str}
    {"type": "presskey_inorder", "keys": list[str]}
    {"type": "presskey_together", "keys": list[str]}
    {"type": "keydown", "key": str}
    {"type": "keyup", "key": str}
    {"type": "wait", "seconds": float}
    {"type": "get_screen_size"} # will return a dict with "width" and "height" keys
    {"type": "continue"} # will return a "continue" back

    Args:
        action_list (list): List of actions to be performed.

    Returns:
        Union[Dict[str, int], str, None]: Returns screen size dict, "continue" string, or None
    """
    try:
        for action_item in action_list:
            action_type = action_item.get("type")
            
            if action_type == "click":
                x, y = action_item.get("x"), action_item.get("y")
                pyautogui.click(x, y)
                
            elif action_type == "mousedown":
                pyautogui.mouseDown()
                
            elif action_type == "mouseup":
                pyautogui.mouseUp()

            elif action_type == "mousemove":
                x, y = action_item.get("x"), action_item.get("y")
                pyautogui.moveTo(x, y)
                
            elif action_type == "scroll":
                x, y = action_item.get("x"), action_item.get("y")
                click_count = action_item.get("click_count", 1)
                pyautogui.scroll(click_count, x=x, y=y)
                
            elif action_type == "input":
                text = action_item.get("text", "")
                pyautogui.typewrite(text)
                
            elif action_type == "presskey_inorder":
                keys = action_item.get("keys", [])
                for key in keys:
                    keyboard.press_and_release(key)
                    time.sleep(0.1)
                    
            elif action_type == "presskey_together":
                keys = action_item.get("keys", [])
                keyboard.press(*keys)
                time.sleep(0.1)
                keyboard.release(*keys)
                
            elif action_type == "keydown":
                key = action_item.get("key")
                keyboard.press(key)
                
            elif action_type == "keyup":
                key = action_item.get("key")
                keyboard.release(key)
                
            elif action_type == "wait":
                seconds = action_item.get("seconds", 1.0)
                time.sleep(seconds)
                
            elif action_type == "get_screen_size":
                width, height = pyautogui.size()
                return {"width": width, "height": height}
                
            elif action_type == "continue":
                return "continue"
                
            else:
                print(f"Unknown action type: {action_type}", file=sys.stderr)
                
        return None
        
    except Exception as e:
        print(f"Error executing actions: {e}", file=sys.stderr)
        return None


tools_list = [action]
if __name__ == "__main__":
    from google.genai import types
    print(types.GenerateContentConfig(tools=tools_list))