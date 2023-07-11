title: 10 Years Later
date: 07-07-2023
author: Jorge Garcia
category: Blog
summary: A digital version of the Makers in Chicago presentation board for Sasha and the Maker Showcasers.

Hi, reader!  

My name is J’orge Garcia and from 2013 to 2019 I worked for the Chicago Public Library in various positions including as a Senior Maker Specialist in the CPL Maker Lab. I joined the maker space team about a month after its opening and loved every minute of my time there. You may already know but the project was only going to be a 6-month experiment and here it is 10 years later!  

In February 2014, I attended the second Maker Summit in the lower level of the library, and I was inspired to create Makers in Chicago. I talked all about it for months until Mark Anderson and Sasha Neri gave me the go-ahead and support to start building it. I still remember the first time I mentioned the idea out loud nearly spilling over my drink on Mariella Colon while the team gathered after work. Brandy Agerbeck was nice enough to share a digital version of our conversation map with me, as well as related conversations to help me make connections and realize what the project could be. I presented the project at the following Maker Summit (https://sshchicago.org/2015-chicago-maker-summit/).  

It's gone through different iterations, including once collecting the community’s calendars all into one page. The Smart Chicago Collaborative supported the original WordPress site until 2016 when the organization sunset. The site then shifted to an open-source directory on GitHub. Since then, I’ve had folks ping me via email and in person with updates for the site. Now, I’d like to once again ask the community to help me keep the site as up-to-date as possible. I invite you to join as a contributor!  

Dig into the conversation maps of our 2014 Summit and related conversations and I hope you might find inspiration in them as I did.  

J’orge  
 
[image will go here]  
CPL Maker Lab Staff - 2018 

[Conversation Maps from the 2014 Maker Summit at the Harold Washington Library
and other convenings, all of which inspired the creation of Makers in Chicago.]


## Submitting or Editing a Maker Org  

Makers in Chicago is an open-source project and is publicly available for contributions via GitHub. No software is needed, and anyone can make editing suggestions via the GitHub website with an account. Fork the project or become a project member. The site is built using Pelican Static Site Generator and only a little Markdown is needed, no code. Pelican is based on Python if you want to get fancy with making new tools for the site.  

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
summary: A makerspace with access to laser cutting and 3D printing near the Thorndale Red Line offering after-school programs.
status: hidden
```

For a look at a fully descriptive makerspace, check out South Side Hackerspace as an example.

https://makersinchicago.org/south-side-hackerspace-chicago.html

## Blogging Tools  

In 2019, we thought to do more writing such as by blogging about the maker happenings around town to reinvigorate the site. I started with a piece on the Chicago Tool Library following a presentation in the Harold Washington Library Video Theater. COVID-19 Lockdowns began shortly after, all happenings came to a halt, and I pivoted to birding. I have since become a professional bird photographer and could not continue following the maker scene as close. Blogging tools are built into the site and as a community site, anyone is allowed to be a contributor by submitting a post as a pull request.

Posts should be prepared in Markdown with the following header metadata:

```
title: A Maker Showcase
date: 07-08-2023
author: Your Name
category: Blog
summary: CPL bring the community together for a MakerShare!
```

## Site Management  

#### Edit Approvals  

Sasha Neri and I (J’orge) are admins to the GitHub Repository and would be the ones to push your edits to the site.  

#### If you’re curious about another Makers in Chicago project, socialraspi is Raspberry Pi photo booth that would push the images captured straight to Twitter. With the changes to the social media platform, the project is not expected to work into the future.  

#### Discussion  
If you have questions, comments, or simply wanted to start a conversation, GitHub Issues or Slack are where you want to drop that comment. While email works too, a public-facing discussion is always appreciated.

## Gone Birding  

#### Where am I?  

After mid-2019, and missing my time at the Maker Lab, I began getting interested in birds. Along came the pandemic and I went all in. Now, I am a professional bird photographer serving as a Coordinator for the Birds in My Neighborhood program at Openlands, a Chicagoland environmental organization. I’ve been on Curious City, and WTTW talking about birds, with another WTTW feature coming out later this year.

Today I was called into another conference happening at North Park Village Nature Center, NatureCon, where I’ll be leading a bird walk. I would have loved to be at this gathering, but I don’t think the Maker Lab staff have figured out cloning yet.

This really exemplifies where I’m at with Makers in Chicago. I am distracted by birds—all of them and all day long! That’s why I need your help to maintain the site.

I know it’ll come to no surprise to my former team that I am back at my silo-breaking reach across local organizations, this time around birds. With that attention, I am no longer as well versed with the maker happenings and maker-org updates as I used to be. 

I hope to return one day! I am interested in the intersection of maker education and culture and environmental science. It’s on my to-do list to explore this region and if you’re interested in chatting about it, let’s grab a coffee or take a walk! 

The Maker in Chicago Slack has been quiet, but I have it loaded on my phone and laptops should a conversation start up again.  

You can always reach me at jorge@jorgegarcia.io I am also on Bluesky and Twitter as @yorickgarcia.  You can also sign up for one of my newsletters at: 

tinyletter.com/chicagobirds/  
tinyletter.com/northparkvillagebirding  
amongthebirds.substack.com/ (new with a Pigeon story coming out soon!)  

Thank you for reading!  

J’orge 🐦  
