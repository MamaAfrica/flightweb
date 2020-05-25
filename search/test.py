itineraries= [
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1015",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "900",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "600",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77L",
                            "name": "Boeing 777-200Lr"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "0",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "149894",
                "mark_up_fare": "0",
                "total_fare": "328093",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "85654",
                            "taxes": [
                                "89635"
                            ],
                            "total": "175289"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "64240",
                            "taxes": [
                                "88564"
                            ],
                            "total": "152804"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "328093",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 328093
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "1150",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "900",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:50:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "04:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "612",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:40:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "763",
                            "name": "Boeing 767-300/300ER"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "1",
        "sequence_number": "0",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "149894",
                "mark_up_fare": "0",
                "total_fare": "328093",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "85654",
                            "taxes": [
                                "89635"
                            ],
                            "total": "175289"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "64240",
                            "taxes": [
                                "88564"
                            ],
                            "total": "152804"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "328093",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 328093
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1400",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "15:30:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "KGL",
                                "name": "Kigali-International, Rwanda",
                                "city_code": "",
                                "city_name": "Kigali",
                                "country_code": "RW",
                                "country_name": "Rwanda",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "203",
                        "res_book_desig_code": "L",
                        "flight_duration": "04:30:00",
                        "operating_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "00:30:00",
                            "airport": {
                                "code": "KGL",
                                "name": "Kigali-International, Rwanda",
                                "city_code": "",
                                "city_name": "Kigali",
                                "country_code": "RW",
                                "country_name": "Rwanda",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "08:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": ""
                            }
                        },
                        "flight_number": "304",
                        "res_book_desig_code": "L",
                        "flight_duration": "06:00:00",
                        "operating_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "WB",
        "combination_id": "0",
        "sequence_number": "1",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "181107",
                "mark_up_fare": "0",
                "total_fare": "337246",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "103438",
                            "taxes": [
                                "78714"
                            ],
                            "total": "182152"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "77669",
                            "taxes": [
                                "77425"
                            ],
                            "total": "155094"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "337246",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 337246
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "1410",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "15:30:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "KGL",
                                "name": "Kigali-International, Rwanda",
                                "city_code": "",
                                "city_name": "Kigali",
                                "country_code": "RW",
                                "country_name": "Rwanda",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "203",
                        "res_book_desig_code": "L",
                        "flight_duration": "04:30:00",
                        "operating_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "00:30:00",
                            "airport": {
                                "code": "KGL",
                                "name": "Kigali-International, Rwanda",
                                "city_code": "",
                                "city_name": "Kigali",
                                "country_code": "RW",
                                "country_name": "Rwanda",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "08:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": ""
                            }
                        },
                        "flight_number": "304",
                        "res_book_desig_code": "L",
                        "flight_duration": "06:00:00",
                        "operating_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "WB",
                            "name": "Rwandair Express"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "WB",
        "combination_id": "1",
        "sequence_number": "1",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "181107",
                "mark_up_fare": "0",
                "total_fare": "337246",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "103438",
                            "taxes": [
                                "78714"
                            ],
                            "total": "182152"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "77669",
                            "taxes": [
                                "77425"
                            ],
                            "total": "155094"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "337246",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 337246
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "0955",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "V",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "03:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "910",
                        "res_book_desig_code": "V",
                        "flight_duration": "03:15:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "789",
                            "name": "Boeing 787-9"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "MS",
        "combination_id": "0",
        "sequence_number": "2",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "173486",
                "mark_up_fare": "0",
                "total_fare": "338224",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "99083",
                            "taxes": [
                                "82986"
                            ],
                            "total": "182069"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "74403",
                            "taxes": [
                                "81752"
                            ],
                            "total": "156155"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "338224",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 338224
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1610",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "V",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "04:45:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "10:00:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "901",
                        "res_book_desig_code": "V",
                        "flight_duration": "03:15:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "MS",
        "combination_id": "0",
        "sequence_number": "3",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "173486",
                "mark_up_fare": "0",
                "total_fare": "339572",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "99083",
                            "taxes": [
                                "83660"
                            ],
                            "total": "182743"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "74403",
                            "taxes": [
                                "82426"
                            ],
                            "total": "156829"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "339572",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 339572
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "2110",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "V",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "09:45:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "15:00:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "912",
                        "res_book_desig_code": "V",
                        "flight_duration": "03:15:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "789",
                            "name": "Boeing 787-9"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "MS",
        "combination_id": "1",
        "sequence_number": "3",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "173486",
                "mark_up_fare": "0",
                "total_fare": "339572",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "99083",
                            "taxes": [
                                "83660"
                            ],
                            "total": "182743"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "74403",
                            "taxes": [
                                "82426"
                            ],
                            "total": "156829"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "339572",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 339572
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "2",
                "direction_id": "0",
                "elapsed_time": "2410",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "V",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "12:45:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "18:00:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "905",
                        "res_book_desig_code": "V",
                        "flight_duration": "03:15:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "MS",
        "combination_id": "2",
        "sequence_number": "3",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "173486",
                "mark_up_fare": "0",
                "total_fare": "339572",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "99083",
                            "taxes": [
                                "83660"
                            ],
                            "total": "182743"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "74403",
                            "taxes": [
                                "82426"
                            ],
                            "total": "156829"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "339572",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 339572
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1405",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "12:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "20:00:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "533",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "23:30:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "1A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "05:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "1A"
                            }
                        },
                        "flight_number": "304",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:15:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "KQ",
        "combination_id": "0",
        "sequence_number": "4",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "221756",
                "mark_up_fare": "0",
                "total_fare": "373061",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "126666",
                            "taxes": [
                                "76442"
                            ],
                            "total": "203108"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "95090",
                            "taxes": [
                                "74863"
                            ],
                            "total": "169953"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "373061",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 373061
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "1915",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:10:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "05:30:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "535",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "14:10:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "1A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:25:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "1A"
                            }
                        },
                        "flight_number": "310",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:15:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "788",
                            "name": "Boeing 787-8"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "KQ",
        "combination_id": "1",
        "sequence_number": "4",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "221756",
                "mark_up_fare": "0",
                "total_fare": "373061",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "126666",
                            "taxes": [
                                "76442"
                            ],
                            "total": "203108"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "95090",
                            "taxes": [
                                "74863"
                            ],
                            "total": "169953"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "373061",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 373061
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "2",
                "direction_id": "0",
                "elapsed_time": "2835",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:10:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "05:30:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "535",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "23:30:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "1A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "05:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "1A"
                            }
                        },
                        "flight_number": "304",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:15:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "KQ",
        "combination_id": "2",
        "sequence_number": "4",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "221756",
                "mark_up_fare": "0",
                "total_fare": "373061",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "126666",
                            "taxes": [
                                "76442"
                            ],
                            "total": "203108"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "95090",
                            "taxes": [
                                "74863"
                            ],
                            "total": "169953"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "373061",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 373061
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "3",
                "direction_id": "0",
                "elapsed_time": "2845",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "12:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "20:00:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "533",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "14:10:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "1A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:25:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "1A"
                            }
                        },
                        "flight_number": "310",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:15:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "788",
                            "name": "Boeing 787-8"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "KQ",
        "combination_id": "3",
        "sequence_number": "4",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "221756",
                "mark_up_fare": "0",
                "total_fare": "373061",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "126666",
                            "taxes": [
                                "76442"
                            ],
                            "total": "203108"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "95090",
                            "taxes": [
                                "74863"
                            ],
                            "total": "169953"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "373061",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 373061
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "3705",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "10:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "10:40:00",
                            "airport": {
                                "code": "LFW",
                                "name": "Lome-G Eyadema Intl, Togo",
                                "city_code": "",
                                "city_name": "Lome",
                                "country_code": "TG",
                                "country_name": "Togo",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1021",
                        "res_book_desig_code": "H",
                        "flight_duration": "00:50:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "06:00:00",
                            "airport": {
                                "code": "LFW",
                                "name": "Lome-G Eyadema Intl, Togo",
                                "city_code": "",
                                "city_name": "Lome",
                                "country_code": "TG",
                                "country_name": "Togo",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "14:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": ""
                            }
                        },
                        "flight_number": "519",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:30:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "787",
                            "name": "787  All Series Passenger"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "600",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77L",
                            "name": "Boeing 777-200Lr"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "5",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "149894",
                "mark_up_fare": "0",
                "total_fare": "376245",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "85654",
                            "taxes": [
                                "113711"
                            ],
                            "total": "199365"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "64240",
                            "taxes": [
                                "112640"
                            ],
                            "total": "176880"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "376245",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 376245
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "3840",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "10:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "10:40:00",
                            "airport": {
                                "code": "LFW",
                                "name": "Lome-G Eyadema Intl, Togo",
                                "city_code": "",
                                "city_name": "Lome",
                                "country_code": "TG",
                                "country_name": "Togo",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1021",
                        "res_book_desig_code": "H",
                        "flight_duration": "00:50:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "06:00:00",
                            "airport": {
                                "code": "LFW",
                                "name": "Lome-G Eyadema Intl, Togo",
                                "city_code": "",
                                "city_name": "Lome",
                                "country_code": "TG",
                                "country_name": "Togo",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "14:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": ""
                            }
                        },
                        "flight_number": "519",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:30:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "787",
                            "name": "787  All Series Passenger"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "22:50:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "04:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "612",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:40:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "1",
        "sequence_number": "5",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "149894",
                "mark_up_fare": "0",
                "total_fare": "376245",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "85654",
                            "taxes": [
                                "113711"
                            ],
                            "total": "199365"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "64240",
                            "taxes": [
                                "112640"
                            ],
                            "total": "176880"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "376245",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 376245
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "2",
                "direction_id": "0",
                "elapsed_time": "4955",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "10:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "10:40:00",
                            "airport": {
                                "code": "LFW",
                                "name": "Lome-G Eyadema Intl, Togo",
                                "city_code": "",
                                "city_name": "Lome",
                                "country_code": "TG",
                                "country_name": "Togo",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1021",
                        "res_book_desig_code": "H",
                        "flight_duration": "00:50:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "06:00:00",
                            "airport": {
                                "code": "LFW",
                                "name": "Lome-G Eyadema Intl, Togo",
                                "city_code": "",
                                "city_name": "Lome",
                                "country_code": "TG",
                                "country_name": "Togo",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "14:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": ""
                            }
                        },
                        "flight_number": "519",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:30:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "787",
                            "name": "787  All Series Passenger"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "10:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "15:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "602",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "2",
        "sequence_number": "5",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "149894",
                "mark_up_fare": "0",
                "total_fare": "376245",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "85654",
                            "taxes": [
                                "113711"
                            ],
                            "total": "199365"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "64240",
                            "taxes": [
                                "112640"
                            ],
                            "total": "176880"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "376245",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 376245
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "2305",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "900",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "10:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "15:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "602",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "6",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "200706",
                "mark_up_fare": "0",
                "total_fare": "381446",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "111060",
                            "taxes": [
                                "90905"
                            ],
                            "total": "201965"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "89646",
                            "taxes": [
                                "89835"
                            ],
                            "total": "179481"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "381446",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 381446
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "0705",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "18:10:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "04:15:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "784",
                        "res_book_desig_code": "U",
                        "flight_duration": "07:05:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "0",
        "sequence_number": "7",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "258051",
                "mark_up_fare": "0",
                "total_fare": "469095",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "147354",
                            "taxes": [
                                "106438"
                            ],
                            "total": "253792"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "110697",
                            "taxes": [
                                "104606"
                            ],
                            "total": "215303"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "469095",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 469095
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "0710",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "12:55:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "23:05:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "782",
                        "res_book_desig_code": "U",
                        "flight_duration": "07:10:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "1",
        "sequence_number": "7",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "258051",
                "mark_up_fare": "0",
                "total_fare": "469095",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "147354",
                            "taxes": [
                                "106438"
                            ],
                            "total": "253792"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "110697",
                            "taxes": [
                                "104606"
                            ],
                            "total": "215303"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "469095",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 469095
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "2305",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1203",
                        "res_book_desig_code": "V",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "10:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "15:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "602",
                        "res_book_desig_code": "T",
                        "flight_duration": "04:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "8",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "352415",
                "mark_up_fare": "0",
                "total_fare": "542265",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "201432",
                            "taxes": [
                                "96186"
                            ],
                            "total": "297618"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "150983",
                            "taxes": [
                                "93664"
                            ],
                            "total": "244647"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "542265",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 542265
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1015",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "900",
                        "res_book_desig_code": "T",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "1109",
                        "res_book_desig_code": "V",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "KP",
        "combination_id": "0",
        "sequence_number": "9",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "352415",
                "mark_up_fare": "0",
                "total_fare": "542265",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "201432",
                            "taxes": [
                                "96186"
                            ],
                            "total": "297618"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "150983",
                            "taxes": [
                                "93664"
                            ],
                            "total": "244647"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "542265",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 542265
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1015",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1203",
                        "res_book_desig_code": "V",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "1109",
                        "res_book_desig_code": "V",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "KP",
        "combination_id": "0",
        "sequence_number": "10",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "352415",
                "mark_up_fare": "0",
                "total_fare": "542265",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "201432",
                            "taxes": [
                                "96186"
                            ],
                            "total": "297618"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "150983",
                            "taxes": [
                                "93664"
                            ],
                            "total": "244647"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "542265",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 542265
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "3115",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "14:10:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:25:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "808",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "600",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77L",
                            "name": "Boeing 777-200Lr"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "11",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "365118",
                "mark_up_fare": "0",
                "total_fare": "613505",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "208691",
                            "taxes": [
                                "125500"
                            ],
                            "total": "334191"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "156427",
                            "taxes": [
                                "122887"
                            ],
                            "total": "279314"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "613505",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 613505
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "3115",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "08:20:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "14:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "848",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:25:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "600",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77L",
                            "name": "Boeing 777-200Lr"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "1",
        "sequence_number": "11",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "365118",
                "mark_up_fare": "0",
                "total_fare": "613505",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "208691",
                            "taxes": [
                                "125500"
                            ],
                            "total": "334191"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "156427",
                            "taxes": [
                                "122887"
                            ],
                            "total": "279314"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "613505",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 613505
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "2",
                "direction_id": "0",
                "elapsed_time": "3250",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "14:10:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:25:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "808",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "22:50:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "04:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "612",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:40:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "2",
        "sequence_number": "11",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "365118",
                "mark_up_fare": "0",
                "total_fare": "613505",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "208691",
                            "taxes": [
                                "125500"
                            ],
                            "total": "334191"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "156427",
                            "taxes": [
                                "122887"
                            ],
                            "total": "279314"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "613505",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 613505
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "3",
                "direction_id": "0",
                "elapsed_time": "4405",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "23:00:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "05:25:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "858",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:25:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "10:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "15:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "602",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "3",
        "sequence_number": "11",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "365118",
                "mark_up_fare": "0",
                "total_fare": "613505",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "208691",
                            "taxes": [
                                "125500"
                            ],
                            "total": "334191"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "156427",
                            "taxes": [
                                "122887"
                            ],
                            "total": "279314"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "613505",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 613505
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1650",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "L",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "23:45:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "03:05:00",
                            "airport": {
                                "code": "RUH",
                                "name": "Riyadh-King Khalid Intl, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Riyadh",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "649",
                        "res_book_desig_code": "K",
                        "flight_duration": "02:20:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "07:45:00",
                            "airport": {
                                "code": "RUH",
                                "name": "Riyadh-King Khalid Intl, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Riyadh",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "10:40:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": ""
                            }
                        },
                        "flight_number": "201",
                        "res_book_desig_code": "E",
                        "flight_duration": "01:55:00",
                        "operating_airline": {
                            "code": "XY",
                            "name": "Flynas"
                        },
                        "equipment": {
                            "code": "320",
                            "name": "Airbus Industrie A320"
                        },
                        "marketing_airline": {
                            "code": "XY",
                            "name": "Flynas"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "XY",
        "combination_id": "0",
        "sequence_number": "12",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "485977",
                "mark_up_fare": "0",
                "total_fare": "613625",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "277649",
                            "taxes": [
                                "65557"
                            ],
                            "total": "343206"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "208328",
                            "taxes": [
                                "62091"
                            ],
                            "total": "270419"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "613625",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 613625
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1910",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:15:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "05:05:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "61",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:50:00",
                        "operating_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "10:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "B"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:25:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "B"
                            }
                        },
                        "flight_number": "7153",
                        "res_book_desig_code": "T",
                        "flight_duration": "08:00:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "SA",
        "combination_id": "0",
        "sequence_number": "13",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "423914",
                "mark_up_fare": "0",
                "total_fare": "649790",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "242081",
                            "taxes": [
                                "114444"
                            ],
                            "total": "356525"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "111432"
                            ],
                            "total": "293265"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "649790",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 649790
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "3100",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:15:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "05:05:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "61",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:50:00",
                        "operating_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "22:20:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "B"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "08:15:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "B"
                            }
                        },
                        "flight_number": "7162",
                        "res_book_desig_code": "T",
                        "flight_duration": "07:55:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "SA",
        "combination_id": "0",
        "sequence_number": "14",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "423914",
                "mark_up_fare": "0",
                "total_fare": "659232",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "242081",
                            "taxes": [
                                "119165"
                            ],
                            "total": "361246"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "116153"
                            ],
                            "total": "297986"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "659232",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 659232
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "2230",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:15:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "05:05:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "61",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:50:00",
                        "operating_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "13:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "B"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "23:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "B"
                            }
                        },
                        "flight_number": "7160",
                        "res_book_desig_code": "T",
                        "flight_duration": "08:20:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "388",
                            "name": "Airbus Industrie A380-800 Passenger"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "SA",
        "combination_id": "0",
        "sequence_number": "15",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "423914",
                "mark_up_fare": "0",
                "total_fare": "659232",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "242081",
                            "taxes": [
                                "119165"
                            ],
                            "total": "361246"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "116153"
                            ],
                            "total": "297986"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "659232",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 659232
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "2750",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:15:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "05:05:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "61",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:50:00",
                        "operating_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "18:50:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "B"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "05:05:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "B"
                            }
                        },
                        "flight_number": "7158",
                        "res_book_desig_code": "T",
                        "flight_duration": "08:15:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "388",
                            "name": "Airbus Industrie A380-800 Passenger"
                        },
                        "marketing_airline": {
                            "code": "SA",
                            "name": "South African Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "SA",
        "combination_id": "1",
        "sequence_number": "15",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "423914",
                "mark_up_fare": "0",
                "total_fare": "659232",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "242081",
                            "taxes": [
                                "119165"
                            ],
                            "total": "361246"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "116153"
                            ],
                            "total": "297986"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "659232",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 659232
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "3250",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "08:20:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "14:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "848",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:25:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "22:50:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "04:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "612",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:40:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "16",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "415929",
                "mark_up_fare": "0",
                "total_fare": "666856",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "234096",
                            "taxes": [
                                "126770"
                            ],
                            "total": "360866"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "124157"
                            ],
                            "total": "305990"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "666856",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 666856
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "4405",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "14:10:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:25:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "808",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "10:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "15:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "602",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "1",
        "sequence_number": "16",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "415929",
                "mark_up_fare": "0",
                "total_fare": "666856",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "234096",
                            "taxes": [
                                "126770"
                            ],
                            "total": "360866"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "124157"
                            ],
                            "total": "305990"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "666856",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 666856
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "2",
                "direction_id": "0",
                "elapsed_time": "4405",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "08:20:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "14:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "848",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:25:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "10:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "15:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "602",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "2",
        "sequence_number": "16",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "415929",
                "mark_up_fare": "0",
                "total_fare": "666856",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "234096",
                            "taxes": [
                                "126770"
                            ],
                            "total": "360866"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "124157"
                            ],
                            "total": "305990"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "666856",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 666856
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "3",
                "direction_id": "0",
                "elapsed_time": "5515",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "23:00:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "05:25:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "858",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:25:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-29",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "600",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77L",
                            "name": "Boeing 777-200Lr"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "3",
        "sequence_number": "16",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "415929",
                "mark_up_fare": "0",
                "total_fare": "666856",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "234096",
                            "taxes": [
                                "126770"
                            ],
                            "total": "360866"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "124157"
                            ],
                            "total": "305990"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "666856",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 666856
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "4",
                "direction_id": "0",
                "elapsed_time": "5650",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "01:25:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "V",
                        "flight_duration": "07:45:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "23:00:00",
                            "airport": {
                                "code": "JNB",
                                "name": "Johannesburg-O.R. Tambo Intl, South Africa",
                                "city_code": "",
                                "city_name": "Johannesburg",
                                "country_code": "ZA",
                                "country_name": "South Africa",
                                "terminal": "A"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "05:25:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "A"
                            }
                        },
                        "flight_number": "858",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:25:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "22:50:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-29",
                            "time": "04:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "612",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:40:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "4",
        "sequence_number": "16",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "415929",
                "mark_up_fare": "0",
                "total_fare": "666856",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "234096",
                            "taxes": [
                                "126770"
                            ],
                            "total": "360866"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "181833",
                            "taxes": [
                                "124157"
                            ],
                            "total": "305990"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "666856",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 666856
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1015",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1203",
                        "res_book_desig_code": "K",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "600",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77L",
                            "name": "Boeing 777-200Lr"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "17",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "492872",
                "mark_up_fare": "0",
                "total_fare": "689745",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "281641",
                            "taxes": [
                                "100197"
                            ],
                            "total": "381838"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "211231",
                            "taxes": [
                                "96676"
                            ],
                            "total": "307907"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "689745",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 689745
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "1150",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "13:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:00:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1203",
                        "res_book_desig_code": "K",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:50:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "04:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "612",
                        "res_book_desig_code": "H",
                        "flight_duration": "04:40:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "763",
                            "name": "Boeing 767-300/300ER"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "1",
        "sequence_number": "17",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "492872",
                "mark_up_fare": "0",
                "total_fare": "689745",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "281641",
                            "taxes": [
                                "100197"
                            ],
                            "total": "381838"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "211231",
                            "taxes": [
                                "96676"
                            ],
                            "total": "307907"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            },
                            {
                                "ticket_designator_code": "79|SUR",
                                "ticket_designator_extension": "FARE VALID FOR E TICKET ONLY|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "689745",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 689745
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1225",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "L",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "00:45:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "06:15:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "926",
                        "res_book_desig_code": "R",
                        "flight_duration": "03:30:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "0",
        "sequence_number": "18",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "576712",
                "mark_up_fare": "0",
                "total_fare": "709782",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "329550",
                            "taxes": [
                                "68595"
                            ],
                            "total": "398145"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "247162",
                            "taxes": [
                                "64475"
                            ],
                            "total": "311637"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "709782",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 709782
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "2355",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "L",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "12:25:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "17:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "928",
                        "res_book_desig_code": "R",
                        "flight_duration": "03:20:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "0",
        "sequence_number": "19",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "576712",
                "mark_up_fare": "0",
                "total_fare": "711130",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "329550",
                            "taxes": [
                                "69269"
                            ],
                            "total": "398819"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "247162",
                            "taxes": [
                                "65149"
                            ],
                            "total": "312311"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "711130",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 711130
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "3100",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "L",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "19:20:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "00:50:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "924",
                        "res_book_desig_code": "R",
                        "flight_duration": "03:30:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "1",
        "sequence_number": "19",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "576712",
                "mark_up_fare": "0",
                "total_fare": "711130",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "329550",
                            "taxes": [
                                "69269"
                            ],
                            "total": "398819"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "247162",
                            "taxes": [
                                "65149"
                            ],
                            "total": "312311"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "711130",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 711130
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "2915",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "07:10:00",
                            "airport": {
                                "code": "IST",
                                "name": "Istanbul-Ataturk, Turkey",
                                "city_code": "",
                                "city_name": "Istanbul",
                                "country_code": "TR",
                                "country_name": "Turkey",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "626",
                        "res_book_desig_code": "M",
                        "flight_duration": "06:30:00",
                        "operating_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "equipment": {
                            "code": "332",
                            "name": "Airbus Industrie A330-200"
                        },
                        "marketing_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "01:25:00",
                            "airport": {
                                "code": "IST",
                                "name": "Istanbul-Ataturk, Turkey",
                                "city_code": "",
                                "city_name": "Istanbul",
                                "country_code": "TR",
                                "country_name": "Turkey",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "06:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": ""
                            }
                        },
                        "flight_number": "762",
                        "res_book_desig_code": "M",
                        "flight_duration": "04:30:00",
                        "operating_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "TK",
        "combination_id": "0",
        "sequence_number": "20",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "598488",
                "mark_up_fare": "0",
                "total_fare": "789440",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "341889",
                            "taxes": [
                                "97608"
                            ],
                            "total": "439497"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "40|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|25DEC19| - SEE ADV PURCHASE|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "256599",
                            "taxes": [
                                "93344"
                            ],
                            "total": "349943"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "40|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|25DEC19| - SEE ADV PURCHASE|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "789440",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 789440
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "2325",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "07:10:00",
                            "airport": {
                                "code": "IST",
                                "name": "Istanbul-Ataturk, Turkey",
                                "city_code": "",
                                "city_name": "Istanbul",
                                "country_code": "TR",
                                "country_name": "Turkey",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "626",
                        "res_book_desig_code": "M",
                        "flight_duration": "06:30:00",
                        "operating_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "equipment": {
                            "code": "332",
                            "name": "Airbus Industrie A330-200"
                        },
                        "marketing_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "19:35:00",
                            "airport": {
                                "code": "IST",
                                "name": "Istanbul-Ataturk, Turkey",
                                "city_code": "",
                                "city_name": "Istanbul",
                                "country_code": "TR",
                                "country_name": "Turkey",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "01:05:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": ""
                            }
                        },
                        "flight_number": "760",
                        "res_book_desig_code": "M",
                        "flight_duration": "04:30:00",
                        "operating_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "TK",
        "combination_id": "0",
        "sequence_number": "21",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "598488",
                "mark_up_fare": "0",
                "total_fare": "789440",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "341889",
                            "taxes": [
                                "97608"
                            ],
                            "total": "439497"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "40|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|25DEC19| - SEE ADV PURCHASE|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "256599",
                            "taxes": [
                                "93344"
                            ],
                            "total": "349943"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "40|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|25DEC19| - SEE ADV PURCHASE|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "789440",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 789440
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "2610",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "07:10:00",
                            "airport": {
                                "code": "IST",
                                "name": "Istanbul-Ataturk, Turkey",
                                "city_code": "",
                                "city_name": "Istanbul",
                                "country_code": "TR",
                                "country_name": "Turkey",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "626",
                        "res_book_desig_code": "M",
                        "flight_duration": "06:30:00",
                        "operating_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "equipment": {
                            "code": "332",
                            "name": "Airbus Industrie A330-200"
                        },
                        "marketing_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "22:20:00",
                            "airport": {
                                "code": "SAW",
                                "name": "Istanbul-Sabiha Gokcen, Turkey",
                                "city_code": "",
                                "city_name": "",
                                "country_code": "",
                                "country_name": "",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "03:50:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": ""
                            }
                        },
                        "flight_number": "758",
                        "res_book_desig_code": "M",
                        "flight_duration": "04:30:00",
                        "operating_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "equipment": {
                            "code": "73H",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "TK",
                            "name": "Turkish Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "TK",
        "combination_id": "0",
        "sequence_number": "22",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "598488",
                "mark_up_fare": "0",
                "total_fare": "793852",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "341889",
                            "taxes": [
                                "99814"
                            ],
                            "total": "441703"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "40|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|25DEC19| - SEE ADV PURCHASE|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "256599",
                            "taxes": [
                                "95550"
                            ],
                            "total": "352149"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "40|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|25DEC19| - SEE ADV PURCHASE|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "793852",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 793852
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "3115",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "18:20:00",
                            "airport": {
                                "code": "LBV",
                                "name": "Leon M'ba Intl",
                                "city_code": "LBV",
                                "city_name": "Libreville",
                                "country_code": "GA",
                                "country_name": "Gabon",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "K",
                        "flight_duration": "01:40:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "12:35:00",
                            "airport": {
                                "code": "LBV",
                                "name": "Leon M'ba Intl",
                                "city_code": "LBV",
                                "city_name": "Libreville",
                                "country_code": "GA",
                                "country_name": "Gabon",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": ""
                            }
                        },
                        "flight_number": "925",
                        "res_book_desig_code": "L",
                        "flight_duration": "05:55:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "788",
                            "name": "Boeing 787-8"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "21:45:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "02:55:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "600",
                        "res_book_desig_code": "L",
                        "flight_duration": "04:10:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "77L",
                            "name": "Boeing 777-200Lr"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "23",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "537514",
                "mark_up_fare": "0",
                "total_fare": "818267",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "307047",
                            "taxes": [
                                "142291"
                            ],
                            "total": "449338"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "230467",
                            "taxes": [
                                "138462"
                            ],
                            "total": "368929"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "818267",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 818267
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "4405",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "18:20:00",
                            "airport": {
                                "code": "LBV",
                                "name": "Leon M'ba Intl",
                                "city_code": "LBV",
                                "city_name": "Libreville",
                                "country_code": "GA",
                                "country_name": "Gabon",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "K",
                        "flight_duration": "01:40:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "12:35:00",
                            "airport": {
                                "code": "LBV",
                                "name": "Leon M'ba Intl",
                                "city_code": "LBV",
                                "city_name": "Libreville",
                                "country_code": "GA",
                                "country_name": "Gabon",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": ""
                            }
                        },
                        "flight_number": "925",
                        "res_book_desig_code": "V",
                        "flight_duration": "05:55:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "788",
                            "name": "Boeing 787-8"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-28",
                            "time": "10:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "15:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "602",
                        "res_book_desig_code": "V",
                        "flight_duration": "04:15:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "",
                            "name": ""
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "24",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "543684",
                "mark_up_fare": "0",
                "total_fare": "824746",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "307047",
                            "taxes": [
                                "142291"
                            ],
                            "total": "449338"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "236637",
                            "taxes": [
                                "138771"
                            ],
                            "total": "375408"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "824746",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 824746
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "3250",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "16:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "18:20:00",
                            "airport": {
                                "code": "LBV",
                                "name": "Leon M'ba Intl",
                                "city_code": "LBV",
                                "city_name": "Libreville",
                                "country_code": "GA",
                                "country_name": "Gabon",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1020",
                        "res_book_desig_code": "K",
                        "flight_duration": "01:40:00",
                        "operating_airline": {
                            "code": "KP",
                            "name": "Asky"
                        },
                        "equipment": {
                            "code": "737",
                            "name": "Boeing 737 (All Series-Stage 3)"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "12:35:00",
                            "airport": {
                                "code": "LBV",
                                "name": "Leon M'ba Intl",
                                "city_code": "LBV",
                                "city_name": "Libreville",
                                "country_code": "GA",
                                "country_name": "Gabon",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "20:30:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": ""
                            }
                        },
                        "flight_number": "925",
                        "res_book_desig_code": "K",
                        "flight_duration": "05:55:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "788",
                            "name": "Boeing 787-8"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "22:50:00",
                            "airport": {
                                "code": "ADD",
                                "name": "Addis Ababa-Bole Intl, Ethiopia",
                                "city_code": "",
                                "city_name": "Addis Ababa",
                                "country_code": "ET",
                                "country_name": "Ethiopia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-28",
                            "time": "04:30:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "612",
                        "res_book_desig_code": "K",
                        "flight_duration": "04:40:00",
                        "operating_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "ET",
                            "name": "Ethiopian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "ET",
        "combination_id": "0",
        "sequence_number": "25",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "604295",
                "mark_up_fare": "0",
                "total_fare": "888388",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "345156",
                            "taxes": [
                                "144197"
                            ],
                            "total": "489353"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "259139",
                            "taxes": [
                                "139896"
                            ],
                            "total": "399035"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "888388",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 888388
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1535",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "L",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "23:45:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "03:05:00",
                            "airport": {
                                "code": "RUH",
                                "name": "Riyadh-King Khalid Intl, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Riyadh",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "649",
                        "res_book_desig_code": "K",
                        "flight_duration": "02:20:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "06:30:00",
                            "airport": {
                                "code": "RUH",
                                "name": "Riyadh-King Khalid Intl, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Riyadh",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": "2"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "09:25:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "2"
                            }
                        },
                        "flight_number": "562",
                        "res_book_desig_code": "Y",
                        "flight_duration": "01:55:00",
                        "operating_airline": {
                            "code": "SV",
                            "name": "Saudi Arabian Airlines"
                        },
                        "equipment": {
                            "code": "320",
                            "name": "Airbus Industrie A320"
                        },
                        "marketing_airline": {
                            "code": "SV",
                            "name": "Saudi Arabian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "MS",
        "combination_id": "0",
        "sequence_number": "26",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "691764",
                "mark_up_fare": "0",
                "total_fare": "921410",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "395242",
                            "taxes": [
                                "117291"
                            ],
                            "total": "512533"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "296522",
                            "taxes": [
                                "112355"
                            ],
                            "total": "408877"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "71|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON REFUNDABLE AFTER DEPARTURE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "921410",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 921410
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1010",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "17:10:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "17:10:00",
                            "airport": {
                                "code": "ACC",
                                "name": "Accra-Kotoka Intl, Ghana",
                                "city_code": "",
                                "city_name": "Accra",
                                "country_code": "GH",
                                "country_name": "Ghana",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "219",
                        "res_book_desig_code": "N",
                        "flight_duration": "01:00:00",
                        "operating_airline": {
                            "code": "AW",
                            "name": "Africa World Airlines"
                        },
                        "equipment": {
                            "code": "ER4",
                            "name": "Embraer Rj145"
                        },
                        "marketing_airline": {
                            "code": "AW",
                            "name": "Africa World Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "18:50:00",
                            "airport": {
                                "code": "ACC",
                                "name": "Accra-Kotoka Intl, Ghana",
                                "city_code": "",
                                "city_name": "Accra",
                                "country_code": "GH",
                                "country_name": "Ghana",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "06:20:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "788",
                        "res_book_desig_code": "U",
                        "flight_duration": "07:30:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "0",
        "sequence_number": "27",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "728057",
                "mark_up_fare": "0",
                "total_fare": "923731",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "415929",
                            "taxes": [
                                "100432"
                            ],
                            "total": "516361"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "312128",
                            "taxes": [
                                "95242"
                            ],
                            "total": "407370"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "923731",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 923731
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "1300",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:20:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "14:20:00",
                            "airport": {
                                "code": "ACC",
                                "name": "Accra-Kotoka Intl, Ghana",
                                "city_code": "",
                                "city_name": "Accra",
                                "country_code": "GH",
                                "country_name": "Ghana",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "217",
                        "res_book_desig_code": "N",
                        "flight_duration": "01:00:00",
                        "operating_airline": {
                            "code": "AW",
                            "name": "Africa World Airlines"
                        },
                        "equipment": {
                            "code": "ER4",
                            "name": "Embraer Rj145"
                        },
                        "marketing_airline": {
                            "code": "AW",
                            "name": "Africa World Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "18:50:00",
                            "airport": {
                                "code": "ACC",
                                "name": "Accra-Kotoka Intl, Ghana",
                                "city_code": "",
                                "city_name": "Accra",
                                "country_code": "GH",
                                "country_name": "Ghana",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "06:20:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "788",
                        "res_book_desig_code": "U",
                        "flight_duration": "07:30:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "1",
        "sequence_number": "27",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "728057",
                "mark_up_fare": "0",
                "total_fare": "923731",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "415929",
                            "taxes": [
                                "100432"
                            ],
                            "total": "516361"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "312128",
                            "taxes": [
                                "95242"
                            ],
                            "total": "407370"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "923731",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 923731
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "2",
                "direction_id": "0",
                "elapsed_time": "1530",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "11:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "11:50:00",
                            "airport": {
                                "code": "ACC",
                                "name": "Accra-Kotoka Intl, Ghana",
                                "city_code": "",
                                "city_name": "Accra",
                                "country_code": "GH",
                                "country_name": "Ghana",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "213",
                        "res_book_desig_code": "N",
                        "flight_duration": "01:00:00",
                        "operating_airline": {
                            "code": "AW",
                            "name": "Africa World Airlines"
                        },
                        "equipment": {
                            "code": "ER4",
                            "name": "Embraer Rj145"
                        },
                        "marketing_airline": {
                            "code": "AW",
                            "name": "Africa World Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "18:50:00",
                            "airport": {
                                "code": "ACC",
                                "name": "Accra-Kotoka Intl, Ghana",
                                "city_code": "",
                                "city_name": "Accra",
                                "country_code": "GH",
                                "country_name": "Ghana",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "06:20:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "788",
                        "res_book_desig_code": "U",
                        "flight_duration": "07:30:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "2",
        "sequence_number": "27",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "728057",
                "mark_up_fare": "0",
                "total_fare": "923731",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "415929",
                            "taxes": [
                                "100432"
                            ],
                            "total": "516361"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "312128",
                            "taxes": [
                                "95242"
                            ],
                            "total": "407370"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "70|PEN",
                                "ticket_designator_extension": "TICKETS ARE NON-REFUNDABLE|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "923731",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 923731
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1655",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "23:20:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "02:30:00",
                            "airport": {
                                "code": "JED",
                                "name": "Jeddah-King Abdulaziz Int, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Jeddah",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "663",
                        "res_book_desig_code": "H",
                        "flight_duration": "02:10:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "330",
                            "name": "Airbus Industrie A330"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "07:00:00",
                            "airport": {
                                "code": "JED",
                                "name": "Jeddah-King Abdulaziz Int, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Jeddah",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": "S"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "10:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "S"
                            }
                        },
                        "flight_number": "566",
                        "res_book_desig_code": "Y",
                        "flight_duration": "02:45:00",
                        "operating_airline": {
                            "code": "SV",
                            "name": "Saudi Arabian Airlines"
                        },
                        "equipment": {
                            "code": "320",
                            "name": "Airbus Industrie A320"
                        },
                        "marketing_airline": {
                            "code": "SV",
                            "name": "Saudi Arabian Airlines"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "MS",
        "combination_id": "0",
        "sequence_number": "28",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "933845",
                "mark_up_fare": "0",
                "total_fare": "1175595",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "533522",
                            "taxes": [
                                "124205"
                            ],
                            "total": "657727"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "75|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES - CHECK RULES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "400323",
                            "taxes": [
                                "117545"
                            ],
                            "total": "517868"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "75|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES - CHECK RULES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1175595",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 1175595
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1305",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "12:40:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "20:00:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "533",
                        "res_book_desig_code": "B",
                        "flight_duration": "05:20:00",
                        "operating_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "KQ",
                            "name": "Kenya Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "22:45:00",
                            "airport": {
                                "code": "NBO",
                                "name": "Nairobi-Jomo Kenyatta, Kenya",
                                "city_code": "",
                                "city_name": "Nairobi",
                                "country_code": "KE",
                                "country_name": "Kenya",
                                "terminal": "1B"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "04:45:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "1B"
                            }
                        },
                        "flight_number": "722",
                        "res_book_desig_code": "U",
                        "flight_duration": "05:00:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "77W",
                            "name": "Boeing 777-300Er"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "0",
        "sequence_number": "29",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1227826",
                "mark_up_fare": "0",
                "total_fare": "1347119",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "701563",
                            "taxes": [
                                "64029"
                            ],
                            "total": "765592"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "526263",
                            "taxes": [
                                "55264"
                            ],
                            "total": "581527"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1347119",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 1347119
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1310",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "23:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "06:20:00",
                            "airport": {
                                "code": "FRA",
                                "name": "Frankfurt-Frankfurt Intl, Germany",
                                "city_code": "",
                                "city_name": "Frankfurt",
                                "country_code": "DE",
                                "country_name": "Germany",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "569",
                        "res_book_desig_code": "Y",
                        "flight_duration": "06:30:00",
                        "operating_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "2",
                                    "quantity": "1",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "08:00:00",
                            "airport": {
                                "code": "FRA",
                                "name": "Frankfurt-Frankfurt Intl, Germany",
                                "city_code": "",
                                "city_name": "Frankfurt",
                                "country_code": "DE",
                                "country_name": "Germany",
                                "terminal": "1"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "16:00:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "1"
                            }
                        },
                        "flight_number": "4626",
                        "res_book_desig_code": "Y",
                        "flight_duration": "05:00:00",
                        "operating_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "2",
                                    "quantity": "1",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "LH",
        "combination_id": "0",
        "sequence_number": "30",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "973768",
                "mark_up_fare": "0",
                "total_fare": "1358903",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "556387",
                            "taxes": [
                                "196043"
                            ],
                            "total": "752430"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "76|PEN",
                                "ticket_designator_extension": "SUBJ TO CANCELLATION/CHANGE PENALTY|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "417381",
                            "taxes": [
                                "189092"
                            ],
                            "total": "606473"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "76|PEN",
                                "ticket_designator_extension": "SUBJ TO CANCELLATION/CHANGE PENALTY|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1358903",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 1358903
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "1",
                "direction_id": "0",
                "elapsed_time": "1310",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "23:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "06:20:00",
                            "airport": {
                                "code": "FRA",
                                "name": "Frankfurt-Frankfurt Intl, Germany",
                                "city_code": "",
                                "city_name": "Frankfurt",
                                "country_code": "DE",
                                "country_name": "Germany",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "569",
                        "res_book_desig_code": "Y",
                        "flight_duration": "06:30:00",
                        "operating_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "2",
                                    "quantity": "1",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "09:00:00",
                            "airport": {
                                "code": "FRA",
                                "name": "Frankfurt-Frankfurt Intl, Germany",
                                "city_code": "",
                                "city_name": "Frankfurt",
                                "country_code": "DE",
                                "country_name": "Germany",
                                "terminal": "1"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "16:00:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "1"
                            }
                        },
                        "flight_number": "5012",
                        "res_book_desig_code": "Y",
                        "flight_duration": "04:00:00",
                        "operating_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "equipment": {
                            "code": "333",
                            "name": "AIRBUS INDUSTRIE A330-300"
                        },
                        "marketing_airline": {
                            "code": "LH",
                            "name": "Lufthansa"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "2",
                                    "quantity": "1",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "LH",
        "combination_id": "1",
        "sequence_number": "30",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "973768",
                "mark_up_fare": "0",
                "total_fare": "1358903",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "556387",
                            "taxes": [
                                "196043"
                            ],
                            "total": "752430"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "76|PEN",
                                "ticket_designator_extension": "SUBJ TO CANCELLATION/CHANGE PENALTY|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "417381",
                            "taxes": [
                                "189092"
                            ],
                            "total": "606473"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "76|PEN",
                                "ticket_designator_extension": "SUBJ TO CANCELLATION/CHANGE PENALTY|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1358903",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 1358903
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1410",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "14:50:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-26",
                            "time": "21:30:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "876",
                        "res_book_desig_code": "H",
                        "flight_duration": "05:40:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "738",
                            "name": "Boeing 737-800"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "23:20:00",
                            "airport": {
                                "code": "CAI",
                                "name": "Cairo-Cairo Intl, Egypt",
                                "city_code": "",
                                "city_name": "Cairo",
                                "country_code": "EG",
                                "country_name": "Egypt",
                                "terminal": "3"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "02:30:00",
                            "airport": {
                                "code": "JED",
                                "name": "Jeddah-King Abdulaziz Int, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Jeddah",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": "3"
                            }
                        },
                        "flight_number": "663",
                        "res_book_desig_code": "H",
                        "flight_duration": "02:10:00",
                        "operating_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "equipment": {
                            "code": "330",
                            "name": "Airbus Industrie A330"
                        },
                        "marketing_airline": {
                            "code": "MS",
                            "name": "Egyptair"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "04:10:00",
                            "airport": {
                                "code": "JED",
                                "name": "Jeddah-King Abdulaziz Int, Saudi Arabia",
                                "city_code": "",
                                "city_name": "Jeddah",
                                "country_code": "SA",
                                "country_name": "Saudi Arabia",
                                "terminal": "N"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "08:00:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "N"
                            }
                        },
                        "flight_number": "802",
                        "res_book_desig_code": "U",
                        "flight_duration": "02:50:00",
                        "operating_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "equipment": {
                            "code": "388",
                            "name": "Airbus Industrie A380-800 Passenger"
                        },
                        "marketing_airline": {
                            "code": "EK",
                            "name": "Emirates"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "1",
                                    "quantity": "2",
                                    "unit": "PC"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "M",
                                "res_book_desig_cabin_name": "Economy"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "EK",
        "combination_id": "0",
        "sequence_number": "31",
        "cabin": {
            "code": "M",
            "name": "Economy"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1220567",
                "mark_up_fare": "0",
                "total_fare": "1418803",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "696482",
                            "taxes": [
                                "103428"
                            ],
                            "total": "799910"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "524085",
                            "taxes": [
                                "94808"
                            ],
                            "total": "618893"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1418803",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 1418803
            }
        }
    },
    {
        "origin_destinations": [
            {
                "ref_number": "0",
                "direction_id": "0",
                "elapsed_time": "1535",
                "segments": [
                    {
                        "departure": {
                            "date": "2019-12-26",
                            "time": "18:00:00",
                            "airport": {
                                "code": "LOS",
                                "name": "Lagos-Murtala Muhammed Intl, Nigeria",
                                "city_code": "",
                                "city_name": "Lagos",
                                "country_code": "NG",
                                "country_name": "Nigeria",
                                "terminal": "I"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "04:40:00",
                            "airport": {
                                "code": "DOH",
                                "name": "Doha-Doha Intl, Qatar",
                                "city_code": "",
                                "city_name": "Doha",
                                "country_code": "QA",
                                "country_name": "Qatar",
                                "terminal": "I"
                            }
                        },
                        "flight_number": "1410",
                        "res_book_desig_code": "D",
                        "flight_duration": "08:40:00",
                        "operating_airline": {
                            "code": "QR",
                            "name": "Qatar Airways"
                        },
                        "equipment": {
                            "code": "788",
                            "name": "Boeing 787-8"
                        },
                        "marketing_airline": {
                            "code": "QR",
                            "name": "Qatar Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "3",
                                    "quantity": "65",
                                    "unit": "KG"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "C",
                                "res_book_desig_cabin_name": "Business"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "C",
                                "res_book_desig_cabin_name": "Business"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "06:30:00",
                            "airport": {
                                "code": "DOH",
                                "name": "Doha-Doha Intl, Qatar",
                                "city_code": "",
                                "city_name": "Doha",
                                "country_code": "QA",
                                "country_name": "Qatar",
                                "terminal": ""
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "08:00:00",
                            "airport": {
                                "code": "KWI",
                                "name": "Kuwait-Kuwait Intl, Kuwait",
                                "city_code": "",
                                "city_name": "Kuwait",
                                "country_code": "KW",
                                "country_name": "Kuwait",
                                "terminal": ""
                            }
                        },
                        "flight_number": "1084",
                        "res_book_desig_code": "P",
                        "flight_duration": "01:30:00",
                        "operating_airline": {
                            "code": "QR",
                            "name": "Qatar Airways"
                        },
                        "equipment": {
                            "code": "320",
                            "name": "Airbus Industrie A320"
                        },
                        "marketing_airline": {
                            "code": "QR",
                            "name": "Qatar Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "3",
                                    "quantity": "65",
                                    "unit": "KG"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "F",
                                "res_book_desig_cabin_name": "First"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "F",
                                "res_book_desig_cabin_name": "First"
                            }
                        ]
                    },
                    {
                        "departure": {
                            "date": "2019-12-27",
                            "time": "09:35:00",
                            "airport": {
                                "code": "KWI",
                                "name": "Kuwait-Kuwait Intl, Kuwait",
                                "city_code": "",
                                "city_name": "Kuwait",
                                "country_code": "KW",
                                "country_name": "Kuwait",
                                "terminal": "4"
                            }
                        },
                        "arrival": {
                            "date": "2019-12-27",
                            "time": "12:35:00",
                            "airport": {
                                "code": "DXB",
                                "name": "Dubai-Dubai Intl, United Arab Emirates",
                                "city_code": "",
                                "city_name": "Dubai",
                                "country_code": "AE",
                                "country_name": "United Arab Emirates",
                                "terminal": "4"
                            }
                        },
                        "flight_number": "671",
                        "res_book_desig_code": "C",
                        "flight_duration": "02:00:00",
                        "operating_airline": {
                            "code": "KU",
                            "name": "Kuwait Airways"
                        },
                        "equipment": {
                            "code": "320",
                            "name": "Airbus Industrie A320"
                        },
                        "marketing_airline": {
                            "code": "KU",
                            "name": "Kuwait Airways"
                        },
                        "baggage": [
                            {
                                "type": "ADT",
                                "baggage": {
                                    "index": "3",
                                    "quantity": "65",
                                    "unit": "KG"
                                }
                            }
                        ],
                        "cabins": [
                            {
                                "rph": "ADT",
                                "res_book_desig_cabin_code": "C",
                                "res_book_desig_cabin_name": "Business"
                            },
                            {
                                "rph": "CHD",
                                "res_book_desig_cabin_code": "C",
                                "res_book_desig_cabin_name": "Business"
                            }
                        ]
                    }
                ],
                "option_pricing_info": ""
            }
        ],
        "validating_airline_code": "QR",
        "combination_id": "0",
        "sequence_number": "32",
        "cabin": {
            "code": "C",
            "name": "Business"
        },
        "pricing": {
            "provider": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "1814700",
                "mark_up_fare": "0",
                "total_fare": "2170411",
                "fare_break_down": [
                    {
                        "passenger": {
                            "code": "ADT",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "1036920",
                            "taxes": [
                                "184334"
                            ],
                            "total": "1221254"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    },
                    {
                        "passenger": {
                            "code": "CHD",
                            "quantity": "1"
                        },
                        "provider_fare": {
                            "base": "777780",
                            "taxes": [
                                "171377"
                            ],
                            "total": "949157"
                        },
                        "ticket_designator": [
                            {
                                "ticket_designator_code": "73|PEN",
                                "ticket_designator_extension": "PENALTY APPLIES|"
                            },
                            {
                                "ticket_designator_code": "41|LTD",
                                "ticket_designator_extension": "LAST TKT DTE|26DEC19| - DATE OF ORIGIN|"
                            }
                        ]
                    }
                ]
            },
            "portal_fare": {
                "currency": {
                    "code": "NGN",
                    "unit": "naira",
                    "decimal": 0
                },
                "base_fare": "2170411",
                "mark_up_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "mark_down_fare": {
                    "user": 0,
                    "role": 0,
                    "airline": 0,
                    "cabin": 0,
                    "total": 0
                },
                "vat": 0,
                "total_fare": 2170411
            }
        }
    }
]
print(len(itineraries))
