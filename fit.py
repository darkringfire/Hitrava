import garmin_fit_sdk as fit

stream = fit.Stream.from_file("DATA/from_Strava_Lunch_Hike.fit")
decoder = fit.Decoder(stream)
messages, errors = decoder.read()

for k, v in messages.items():
    print(k)
    # for msg in v:
    #     print("---")
    #     print(msg)
    print("\n")
