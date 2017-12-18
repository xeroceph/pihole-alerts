"""
xeroceph - https://github.com/xeroceph/pihole-alerts
GNU General Public License GPL v3.0 - https://www.gnu.org/licenses/gpl-3.0.en.html
"""

def searchQueries(queries, blacklist):
    result = {}
    for x in blacklist:
        hits = 0
        for i in queries:
            for n in queries[i]:
                if x in n:
                    hits += 1
                    result[x] = hits
    return result

