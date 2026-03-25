import urllib.request
import json

FAL_KEY = "86e710ca-38c6-4a21-b6f0-2703ca56f514:b7a3f6aeb8f53666953504a7e291ac20"

images = [
    ("v5_quiz", "Shocking ad creative, close up of a hand slamming down a premium gold credit card on a table, huge bold red text INSTANTLY APPROVED, white background, $5,000 in large green numbers, red urgent arrow pointing down, clickbait financial ad style"),
    ("v6_quiz", "Urgent ad creative showing a phone screen with CONGRATULATIONS message and confetti, bold red text YOU QUALIFY FOR $7K, green credit card floating out of the screen, white background, exclamation marks, high urgency financial ad"),
    ("v7_quiz", "Dramatic ad with a woman looking shocked at her phone, bold red text BAD CREDIT DOESNT MATTER, subtitle Instant $5K Card Approval, green Apply Now button glowing, white background, emotional clickbait style"),
    ("v5_cards", "Bold ad showing a credit card being cut in half with scissors next to a shiny new gold card, red text DITCH YOUR OLD CARD, subtitle Upgrade to $10K Limit Today, white background, before and after style, urgent"),
    ("v6_cards", "Eye-catching ad with a red ALERT stamp over a stack of credit cards, bold text LAST CHANCE $7,500 LIMIT, subtitle Limited Spots Available, countdown timer showing 03:42, white background, extreme urgency"),
    ("v7_cards", "Dramatic ad with money falling from above onto a gold credit card, bold red text FREE MONEY ALERT, subtitle $200 Cash Bonus Just For Signing Up, green claim button, white background, viral clickbait style"),
    ("v5_score", "Shocking ad showing a credit score of 520 with a green APPROVED stamp over it, bold red text SCORE DOESNT MATTER, subtitle Everyone Gets $5K, green button, white background, impossible-seeming financial ad"),
    ("v6_score", "Urgent ad with a red warning triangle and bold text BANKS HATE THIS, subtitle How People With 550 Scores Get $7K Cards, gold credit card, white background, conspiracy clickbait style"),
    ("v7_score", "Bold ad showing a rejected stamp crossed out and replaced with APPROVED in green, red text DENIED EVERYWHERE ELSE?, subtitle We Say YES Up To $10K, green button, white background, redemption arc style"),
    ("v5_limit", "Extreme ad with giant gold text $10,000 with dollar signs raining down, red text ITS YOURS RIGHT NOW, subtitle No Deposit No Credit Check, green CLAIM IT button pulsing, white background, maximum urgency"),
    ("v6_limit", "Dramatic ad showing a golden credit card emerging from a treasure chest, bold red text HIDDEN $7K CARD, subtitle Banks Dont Advertise This One, green unlock button, white background, secret discovery style"),
    ("v7_limit", "Bold ad with a red countdown timer and text OFFER EXPIRES TONIGHT, subtitle $5,000 Pre-Approved Card Waiting, gold card with sparkle effects, green GRAB IT button, white background, extreme FOMO"),
    ("v5_guide", "Shocking ad with a magnifying glass revealing hidden text on a credit card statement, bold red text THE $500 TRICK, subtitle Credit Card Secret That Saves Thousands, white background, expose style"),
    ("v6_guide", "Bold ad showing a person tearing up a bill with a gold credit card next to them, red text NEVER PAY INTEREST AGAIN, subtitle The Card Trick Nobody Talks About, white background, revolutionary style"),
    ("v7_guide", "Urgent ad with a newspaper headline style layout, bold red text BREAKING: NEW $10K CARD, subtitle No Annual Fee No Credit Check Instant Approval, gold card image, white background, news alert clickbait"),
]

sizes = [("square", "1:1"), ("horizontal", "16:9"), ("vertical", "2:3")]

for name, prompt in images:
    for size_name, aspect in sizes:
        print(f"{name}_{size_name}...", end=" ", flush=True)
        data = json.dumps({"prompt": prompt, "aspect_ratio": aspect, "output_format": "jpeg"}).encode()
        req = urllib.request.Request("https://fal.run/fal-ai/nano-banana-2", data=data,
            headers={"Authorization": f"Key {FAL_KEY}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read())
            if "images" in result and result["images"]:
                print(result["images"][0]["url"])
            else:
                print("NO IMAGE")
        except Exception as e:
            print(f"ERR: {e}")

print("DONE")
