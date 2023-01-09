import cv2
import datetime
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("People Counter")

# Set up the camera
camera = cv2.VideoCapture(0)

# Set up the background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Initialize the count
count = 0

# Set the font for the count label
font = cv2.FONT_HERSHEY_SIMPLEX

# Set the text and background colors for the count label
text_color = (255, 255, 255)
bg_color = (0, 0, 0)

# Set the initial count label text
count_text = "Count: 0"

# Set the count label text position
text_position = (10, 20)

# Set the count label text size
text_size = 0.5

# Set the count label text thickness
text_thickness = 1

# Set the count label text line type
text_line_type = cv2.LINE_AA

def update_count():
  # Get the current frame from the camera
  _, frame = camera.read()

  # Apply the background subtractor to the frame
  fg_mask = bg_subtractor.apply(frame)

  # Count the number of white pixels in the foreground mask
  count = cv2.countNonZero(fg_mask)

  # Update the count label text
  count_text = "Count: " + str(count)

  # Display the count label on the frame
  cv2.putText(frame, count_text, text_position, font, text_size, text_color, text_thickness, text_line_type)

  # Show the frame
  cv2.imshow("Frame", frame)

  # Save the current date and time, along with the count, to a text file
  with open("count.txt", "a") as f:
    f.write(str(datetime.datetime.now()) + ": " + str(count) + "\n")

# Set up the update timer
update_timer = tk.Tk()
update_timer.after(0, update_count)
update_timer.mainloop()

# Release the camera
camera.release()

# Close all windows
cv2.destroyAllWindows()
