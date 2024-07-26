# YoURL
  #### Video Demo:  <URL HERE>
  #### Description: 
  YoURL is a terminal-based web scraping program for YouTube videos, implemented in Python. It allows users to input a YouTube video URL, and the program will return a table with some useful information about the video, such as the subscriber count, the number of likes, whether the video is family-friendly, the genre of the video, the like ratio (how many subscribers are actually liking the video), and the view ratio (how many subscribers are viewing the video).

The program consists of a main function and 14 other functions: verify, title, author, date, isfamily, gen, subscriber, video_id, likes, views, viewRatio, likeRatio, data, and get_request1.

The verify function uses regex to validate a YouTube URL. Other functions like title, author, date, isfamily, and gen use the Beautiful Soup library for web scraping the video. The other functions use the YouTube Data API to retrieve information about the video.

### **Project Requirements:**
- 1 - This Project must be implemented in Python.
- 2 - This Porject should have one main function and at least 14 functions.
- 3 - The test functions of the Project must've be in file called test_project that has another 13 functions that must be executed with pytest, all the functions sould have a **test_** in the begin name of the function.
- 4 - A file callend **requirements.txt** that has all the requirements that you'll need to run this project correctly, this file must be in the root together with **project.py** and **test_project.py**

  
  
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  List of suppoerted Links: 
  
  #https://www.youtube.com/watch?v=iQeBYPJWtak
  
  #http://youtu.be/cCnrX1w5luM
  
  #http://youtube/cCnrX1w5luM 
  
  #youtu.be/cCnrX1w5luM
  
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=43s
  
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ&at=25
  
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1
  
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ#t=1m30s
  
  #https://www.youtube.com/embed/dQw4w9WgXcQ
  
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be
  
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PL9tY0BWXOZFtAk_vlObsc1kYM3Imi2F98&index=3
  
  #https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley
  
  #https://youtu.be/ofmSXnoS7FE?si=FPIUjUDnEqJBzEe4
  
  #https://www.youtube.com/watch?v=hv-hbublepc
  
  #https://www.youtube.com/watch?v=DFYRQ_zQ-gk&feature=featured
  
  #https://m.youtube.com/watch?v=DFYRQ_zQ-gk
  
  #https://www.youtube.com/v/DFYRQ_zQ-gk?fs=1&hl=en_US
  
  #https://www.youtube-nocookie.com/embed/DFYRQ_zQ-gk?autoplay=1
  
