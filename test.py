import metapy
import matplotlib.pyplot as plt

"""
@begin parameter_search @desc Workflow for using ranking function to score the parameter
@param s @desc the parameter s of the ranking function PivotedLength
@in config_file @uri file:config.toml @desc metapy configuration file to do text mining
@out score @desc the final score for ranking function
@out avg_p @desc average precision for every query
@out test.png @uri file: test.png 
"""

def parameter_search(s):
    """
    @begin metapy_run @desc Create metapy idx and queries and using IREval from config files
    @in  config_file @as config_file
    @out idx @desc make inverted index
    @out query @desc build the query object
    @out ev   @desc to do an IR evaluation
    """
    idx=metapy.index.make_inverted_index('config.toml')
    query=metapy.index.Document()
    ev=metapy.index.IREval('config.toml')

    """
    @end metapy_run
    """

    """
    @begin score_calculate @desc calculate scores for queries and plot
    @param num_results @desc loop over the queries file and add each result to the IREval object ev
    @param s
    @in idx 
    @in ev 
    @out score 
    @out avg_p 
    @out test.png 
    """
    num_results=10
    # list_s=[]
    score=[]
    for si in range(len(s)):
        # list_s.append(s)
        ranker=metapy.index.PivotedLength(si)
        with open('cranfield-queries.txt')as query_file:
            for query_num,line in enumerate(query_file):
                query.content(line.strip())
                results=ranker.score(idx,query,num_results)
                avg_p=ev.avg_p(results,query_num,num_results)
                print(avg_p)
        score.append(ev.map())
    plt.plot(s,score,'ro')
    plt.savefig('test.png')
    """
    @end score_calculate
    """

"""
@end parameter_search()
"""



if __name__ == '__main__':
    parameter_search(list(range(10)))

