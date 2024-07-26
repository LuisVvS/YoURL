# YoURL
  #### Video Demo:  <URL HERE>
  #### Description: 
  YoURL is a terminal-based web scraping program for YouTube videos, implemented in Python. It allows users to input a YouTube video URL, and the program will return a table with some useful information about the video, such as the subscriber count, the number of likes, whether the video is family-friendly, the genre of the video, the like ratio (how many subscribers are actually liking the video), and the view ratio (how many subscribers are viewing the video).

The program consists of a `main` function and 14 other functions: `verify`, `title`, `author`, `date`, `isfamily`, `gen`, `subscriber`, `video_id`, `likes`, `views`, `viewRatio`, `likeRatio`, `data`, and `get_request1`.

The verify function uses regex to validate a YouTube URL. Other functions like title, author, date, isfamily, and gen use the Beautiful Soup library for web scraping the video. The other functions use the YouTube Data API to retrieve information about the video.

### **Project Requirements:**
- This project must be implemented in Python.
- This project should have one main function and at least 14 other functions.
- The test functions of the project must be in a file called test_project.py that has another 13 functions which must be executed with pytest. All the functions should have a `test_` prefix in their names.
- A file called requirements.txt should list all the requirements needed to run this project correctly. This file must be in the root directory together with `project.py` and `test_project.py`.

### **Usage:**
1. Clone the repository: `git clone https://github.com/LuisVvS/YoURL.git`
2. Install the required deoendencies with pip: `pip install -r requirements.txt`
3. Run the program with `python project.py` in your terminal to run `project.py`
4. To run the tests run `pytest test_project.py` in your terminal.
5. Enjoy :)

  
  List of suppoerted Links: 
  
  `https://www.youtube.com/watch?v=iQeBYPJWtak`
  
  `http://youtu.be/cCnrX1w5luM`
   
  `youtu.be/cCnrX1w5luM`
  
  `https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=43s`
  
  `https://www.youtube.com/watch?v=dQw4w9WgXcQ&at=25`
  
  `https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1`
  
  `https://www.youtube.com/watch?v=dQw4w9WgXcQ#t=1m30s`
  
  `https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be`
  
  `https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PL9tY0BWXOZFtAk_vlObsc1kYM3Imi2F98&index=3`
  
  `https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley`
  
  `https://youtu.be/ofmSXnoS7FE?si=FPIUjUDnEqJBzEe4`
  
  `https://www.youtube.com/watch?v=hv-hbublepc`
  
  `https://www.youtube.com/watch?v=DFYRQ_zQ-gk&feature=featured`
  
  `https://m.youtube.com/watch?v=DFYRQ_zQ-gk`
  
  `https://www.youtube.com/v/DFYRQ_zQ-gk?fs=1&hl=en_US`
