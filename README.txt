Description:
Create a website that mimics Google's search engine.

Requirement:
Frontend: Should present a simple query interface to the web user, which asks for a single keyword. In response to a user query through a web browser, the frontend should respond by searching the keyword against the indexed database of URLs built by the backend. In addition, the returned URL should be displayed in sorted order according to a ranked score computed in advance by the backend.
Backend: Should take an arbitrary file named urllist.txt, which contains one URL per line, and build an inverted index database which maps keyward to URLs. In addition, each URL needs to be assigned a page rank using page rank algorithm.

Resource:
Frontend: Use the Bottle web framework.
Backend: Take an arbitrary file named urllist.txt, which contains one URL per line, and build an inverted index database which maps keywords to URLs. In addition, each URL needs to be assigned a page rank using PageRank algorithm.

Deliverables:
The project is to be completed in four lab stages. 
