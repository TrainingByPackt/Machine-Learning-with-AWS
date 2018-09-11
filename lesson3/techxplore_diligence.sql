#SELECT * FROM linkedTopicDB2.all_techxplore_articles;

SELECT count(unique_article_id),
		count(distinct(unique_article_id)) 
FROM linkedTopicDB2.all_techxplore_articles;

#SELECT unique_article_id, count(unique_article_id)
#FROM linkedTopicDB2.all_infozine_articles
#group by unique_article_id
#HAVING count(unique_article_id) > 1;


SELECT count(distinct(category)) 
FROM linkedTopicDB2.all_techxplore_articles;