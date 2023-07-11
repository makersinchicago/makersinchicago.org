![Makers in Chicago](/style400/static/images/logotype.png)  
Makers in Chicago serves as a categorized directory of organizations fostering the maker culture in the Chicagoland area. The idea for Makers in Chicago originated from the Institute of Museum and Library Services grant that was awarded to the Chicago Public Library and the work that has come out of the CPL MakerLab that it launch. 

Start up a conversation on http://bit.ly/makersinchicago-slack or submit questions and comments as Issues on GitHub: https://github.com/makersinchicago/makersinchicago.org/issues

Created by jorge@jorgegarcia.io
@yorickgarcia on Bluesky or Twitter

### Managing the Data


Makers in Chicago is an open-source project and is publicly available for contributions via GitHub. No software is needed, and anyone can make editing suggestions via the GitHub website with an account. Fork the project or become a project member. The site is built using Pelican Static Site Generator and only a little Markdown is needed, no code. Pelican is based on Python is you want to get fancy with making new tools for the site.

The data for the directory lives through markdown files in a folder structure. Folders manage the categories. Creating a markdown file in a folder will list a new organization categorized as that folder's name. Creating a new folder would create a new category. The markdown files contain metadata for the organizations and should follow this format:

```
title:  
address:  
tags:  
site:  
summary: 
```

#### Root Folders explained:

**.github** – for managing the Issues Page submission template  
**content** – this is where everything for the site lives.  
**style** – the site’s theme lives here.  

#### Content Folder and the Directory

If you want to begin editing, it’s important to explore the Content folder—more specifically, the directory subfolder. Inside you’ll see Folders that create the site’s categories and inside you’ll find markdown (.md) files. If you want to create a new directory item, you’ll want to make a markdown file in an appropriate folder. Here is an example of Pumping Station 1’s markdown. 

```
title: Pumping Station 1
tags: hackerspace, paid membership, avondale
address: 3519 N Elston Ave, Chicago, IL 60618
summary: The original Chicago hackerspace, take your making to the next level. Two levels of membership. Some events open to the public, including orientations.
site: https://pumpingstationone.org
```

When a location is closed, it is best to add a metadata field that reads “status: hidden”

```
title: Edgewater Workbench
address: 1130 W Thorndale Ave, Chicago, IL 60660
site: http://www.edgewaterworkbench.com/
tags: After School Matters, edgewater
summary: A makerspace with access to laser cutting and 3D printing near the Thorndale Red Line offering after school programs.
status: hidden
```

For a look at a fully descriptive makerspace, check out South Side Hackerspace as an example.

https://makersinchicago.org/south-side-hackerspace-chicago.html
