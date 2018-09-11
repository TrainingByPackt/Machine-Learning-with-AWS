#SELECT * FROM linkedTopicDB2.infozine_articles;


# check for duplicate articles
SELECT count(unique_article_id),
		count(distinct(unique_article_id)) 
FROM linkedTopicDB2.infozine_articles;



# check if description meets 3 sentence requirement (~60 words)
#SELECT (LENGTH(description) - length(replace(description,' ',''))) as description_word_count,
#description
#FROM linkedTopicDB2.infozine_articles;

# check if description meets 3 sentence requirement (~60 words)
#SELECT AVG((LENGTH(description) - length(replace(description,' ','')))) as avg_description_word_count
#FROM linkedTopicDB2.infozine_articles;

#check articles count per category
SELECT count(unique_article_id),
		category
FROM linkedTopicDB2.infozine_articles
group by category;


# check for duplicate articles
SELECT count(link),
		count(distinct(link)) 
FROM linkedTopicDB2.infozine_articles;



SELECT AVG((LENGTH(description) - length(replace(description,' ',''))))
FROM linkedTopicDB2.all_infozine_articles_content;

# verify word count per articles. 
# order by Aescending to verify minimum word_count is above 60 words
SELECT (LENGTH(article_content) - length(replace(article_content,' ',''))) as word_count,
unique_article_id,
article_content
FROM linkedTopicDB2.all_infozine_articles_content
GROUP BY word_count
ORDER BY word_count ASC;

# delete values below the 60 word_count threshold i.e. articles with unique_article_id: 65694 and 67126
DELETE FROM linkedTopicDB2.all_infozine_articles_content
WHERE unique_article_id = '65694';

DELETE FROM linkedTopicDB2.all_infozine_articles_content
WHERE unique_article_id = '67126';

SELECT * FROM linkedTopicDB2.all_infozine_articles_content;

/*
# average wordcount in article_content
SELECT AVG(LENGTH(article_content) - length(replace(article_content,' ',''))+1)
FROM linkedTopicDB2.all_infozine_articles_content;
*/
#SELECT * FROM linkedTopicDB2.all_infozine_articles_content;
