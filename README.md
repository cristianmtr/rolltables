<img align="right" src="https://i.imgur.com/gJRZqTq.png?1">


# RPG Tables

Available at https://cristianmtr.github.io/rpg_tables/

## Features

- tons of random tables
- search for tables
- history of rolls
- easily extendable (tables are in the very readable [JSON format](https://en.wikipedia.org/wiki/JSON#Example))
- static HTML & javascript only (you can download it and it's all yours. No need for active internet connection)
- subtable rolls
- custom ranges in tables

## TODOs

- * tables subrolls. I want to roll all the tables under a category
- fix not being able to have subrolls in separate file

## Collaboration & feedback

Please submit any ideas & feedback you might have as a github issue [here](https://github.com/cristianmtr/rpg_tables/issues/new)

Feel free to have a look at the code and suggest improvements as well.

Check issues and projects for possible ideas to start.

If you want to add your own tables, look at this example: [Planescape NPC](https://github.com/cristianmtr/rpg_tables/blob/ad6a7ebf88f60ddd1986ad7d1b07bf42121e1cae/js/roll_menu.js#L2393)

### Adding a new table

- add a new file `roll_your_type.js`
- add this file to `index.html`, like

```html
  <script src="js/roll_modern_horror.js"></script>
```
- add a case in `rolltables.js`

```js
    case "modern_horror":
        return top.modern_horror;
        break;   
```
- if it's got multiple rolls, you need to add it to `roll_menu.js`, like

```js
   {
        id: "modern_horror",
        title: "Modern Horror",
        items: [
            {
                title: "Gothic All",
                use: "",
                sub_rolls: [
                ],
                main_rolls: [
                    "modern_horror/gothic_motifs",
                    "modern_horror/gothic_events",
                    "modern_horror/gothic_locations",
                    "modern_horror/gothic_buildings",
                    "modern_horror/gothic_parts_buildings",
                ]
            }
        ]
    }
```

### Parse clipboard

Copy a selection of lines.

Use 

`python scripts\parse_clipboard.py gothic_characters "Gothic Characters"`

Contents pasted back to clipboard.

## Credits

Developed based on initial work [here](https://github.com/autorolltables/autorolltables.github.io)

Tables content by:

- OrkishBlade and others from <a href="https://www.reddit.com/r/behindthetables/">/r/behindthetables</a> and <a href="https://www.reddit.com/r/dndbehindthescreen/">/r/dndbehindthescreen</a>
- https://www.enworld.org/threads/list-of-all-personality-traits-ideals-bonds-flaws.469002/
- https://embyr.obsidianportal.com/wikis/npc-occupations
- https://forgottenrealms.fandom.com/wiki/Waterdeep
- https://ynasmidgard.blogspot.com/2016/07/huge-name-list.html
- https://docs.google.com/document/d/1bnH9HP98V8j7SdkJJJiKopWGJ51tG5XN8Bf_RTnj2RQ/edit
- https://www.reddit.com/r/bladesinthedark/comments/fdmqyp/score_generator_inspired_by_leverage_rpgs/
- Godbound (Free Edition), by Kevin Crawford. [https://www.drivethrurpg.com/product/185959/Godbound-A-Game-of-Divine-Heroes-Free-Edition](https://www.drivethrurpg.com/product/185959/Godbound-A-Game-of-Divine-Heroes-Free-Edition)

Top image by https://unsplash.com/@armato
