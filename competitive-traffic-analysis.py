#!/usr/bin/env python3
import requests
import csv
import io

API_KEY = "27a7d67ad96d01bcee72947dc28cfe74"

def get_domain_traffic(domain):
    """Get estimated monthly traffic for a domain based on SEMrush data"""
    url = f"https://api.semrush.com/"
    params = {
        'type': 'domain_organic',
        'key': API_KEY,
        'domain': domain,
        'database': 'us',
        'display_limit': 1000
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.text
            
            # Parse CSV data
            reader = csv.DictReader(io.StringIO(data), delimiter=';')
            
            total_traffic_pct = 0
            keywords = []
            
            for row in reader:
                try:
                    keyword = row['Keyword']
                    position = int(row['Position']) if row['Position'].isdigit() else 999
                    search_vol = int(row['Search Volume']) if row['Search Volume'].isdigit() else 0
                    traffic_pct = float(row['Traffic (%)']) if row['Traffic (%)'] else 0
                    
                    if position <= 20 and search_vol > 0:
                        keywords.append({
                            'keyword': keyword,
                            'position': position, 
                            'search_vol': search_vol,
                            'traffic_pct': traffic_pct
                        })
                        total_traffic_pct += traffic_pct
                        
                except (ValueError, KeyError) as e:
                    continue
            
            # Calculate estimated traffic using largest traffic percentage keyword
            if keywords:
                # Sort by traffic percentage to find the largest contributor
                keywords.sort(key=lambda x: x['traffic_pct'], reverse=True)
                top_keyword = keywords[0]
                
                # Estimate total traffic based on top keyword
                if top_keyword['traffic_pct'] > 0:
                    # Use click-through rate estimation for position 1
                    ctr = 0.28 if top_keyword['position'] == 1 else 0.15 if top_keyword['position'] == 2 else 0.05
                    estimated_clicks_from_keyword = top_keyword['search_vol'] * ctr
                    estimated_total_traffic = (estimated_clicks_from_keyword / top_keyword['traffic_pct']) * 100
                    
                    return {
                        'domain': domain,
                        'total_traffic': int(estimated_total_traffic),
                        'top_keyword': top_keyword['keyword'],
                        'top_keyword_vol': top_keyword['search_vol'],
                        'traffic_pct': top_keyword['traffic_pct'],
                        'total_keywords': len(keywords)
                    }
            
            return None
            
    except Exception as e:
        print(f"Error getting data for {domain}: {e}")
        return None

# Get traffic data for all competitors
competitors = [
    'laykold.com',
    'sportmaster.net', 
    'novasports.com',
    'tru-bounce.com',
    'atsports.com'
]

print("=== COMPETITIVE TRAFFIC ANALYSIS ===\n")

for domain in competitors:
    result = get_domain_traffic(domain)
    if result:
        print(f"{result['domain'].upper()}")
        print(f"  Estimated Monthly Traffic: {result['total_traffic']:,}")
        print(f"  Top Keyword: {result['top_keyword']} ({result['top_keyword_vol']} vol, {result['traffic_pct']:.1f}% of traffic)")
        print(f"  Total Ranking Keywords: {result['total_keywords']}")
        print(f"  Estimated Annual Organic Value: ${result['total_traffic'] * 12 * 3:,}")  # $3 estimated value per visit
        print()
    else:
        print(f"Could not get data for {domain}\n")