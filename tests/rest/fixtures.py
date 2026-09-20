# Auto-generated structure. Fill in the blank values with real test data.
import time

TEST_DATA: dict[str, dict[str, object]] = {
    "accounts.get_accounts": {
        "body": {"account_ids": ["UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0"]},
    },
    "accounts.get_account": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.account_dns_back_resolve": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_jettons_balances": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_jetton_balance": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "jetton_id": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
    },
    "accounts.get_account_jettons_history": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "limit": 10,
    },
    "accounts.get_account_jetton_history_by_id": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "jetton_id": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
        "limit": 10,
    },
    "accounts.get_account_nft_items": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_events": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "limit": 10,
    },
    "accounts.get_account_event": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "event_id": "959ddd8cd66c7ebbe84d00676ddb6fa25ee90199413c467ccc1f25cb21fa0202",
    },
    "accounts.get_account_traces": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_subscriptions": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.reindex_account": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.search_accounts": {
        "name": "ness",
    },
    "accounts.get_account_dns_expiring": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_public_key": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_multisigs": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_diff": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "start_date": int(time.time()) - 84000,
        "end_date": int(time.time()),
    },
    "accounts.get_account_defi_assets": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "accounts.get_account_extra_currency_history_by_id": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "id": 239,
        "limit": 10,
    },
    "accounts.get_jetton_account_history_by_id": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "jetton_id": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
        "limit": 10,
    },
    # "accounts.emulate_message_to_account_event": {
    #     "account_id": "",
    #     "body": {"boc": ""},
    # },
    "blockchain.get_reduced_blockchain_blocks": {
        "from_": int(time.time()) - 600,
        "to": int(time.time()),
    },
    "blockchain.get_block": {
        "block_id": "(-1,8000000000000000,58000381)",
    },
    "blockchain.download_blockchain_block_boc": {
        "block_id": "(-1,8000000000000000,58000381)",
    },
    "blockchain.get_masterchain_shards": {
        "masterchain_seqno": 57981181,
    },
    "blockchain.get_masterchain_blocks": {
        "masterchain_seqno": 57981181,
    },
    "blockchain.get_masterchain_transactions": {
        "masterchain_seqno": 57981181,
    },
    "blockchain.get_config_from_block": {
        "masterchain_seqno": 57981181,
    },
    "blockchain.get_raw_blockchain_config_from_block": {
        "masterchain_seqno": 57981181,
    },
    "blockchain.get_block_transactions": {
        "block_id": "(-1,8000000000000000,58000381)",
    },
    "blockchain.get_transaction": {
        "transaction_id": "959ddd8cd66c7ebbe84d00676ddb6fa25ee90199413c467ccc1f25cb21fa0202",
    },
    "blockchain.get_transaction_by_message_hash": {
        "msg_id": "4eee803beab5a31685b5c06a0716bd770f662db0395acbebc2ee6dd9c8227c34",
    },
    "blockchain.get_raw_account": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "blockchain.get_raw_accounts": {
        "body": {"account_ids": ["UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0"]},
    },
    "blockchain.get_account_transactions": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "blockchain.execute_get_method": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "method_name": "get_public_key",
    },
    "blockchain.execute_get_method_with_body": {
        "account_id": "EQC3dNlesgVD8YbAazcauIrXBPfiVhMMr5YYk2in0Mtsz0Bz",
        "method_name": "dnsresolve",
        "body": {
            "args": [
                {
                    "type": "slice_boc_hex",
                    "value": "b5ee9c7201010101000700000a6e65737300",
                },
                {
                    "type": "int257",
                    "value": "0x19f02441ee588fdb26ee24b2568dd035c3c9206e11ab979be62e55558a1d17ff",
                },
            ]
        },
    },
    # "blockchain.send_message": {
    #     "body": {"boc": "", "batch": [""], "meta": {"additionalProp1": "", "additionalProp2": ""}},
    # },
    "blockchain.account_inspect": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    # "blockchain.get_library_by_hash": {
    #     "hash": "",
    # },
    "connect.get_account_info_by_state_init": {
        "body": {
            "state_init": "te6cckECFgEAArEAAgE0AgEAUYAAAAA///+IvOIjLL7fwNzMP0gs70ruKr3mzxYhjTbYs7u0PB6FzPugART/APSkE/S88sgLAwIBIAYEAQLyBQEeINcLH4IQc2lnbrry4Ip/EQIBSBAHAgEgCQgAGb5fD2omhAgKDrkPoCwCASANCgIBSAwLABGyYvtRNDXCgCAAF7Ml+1E0HHXIdcLH4AIBbg8OABmvHfaiaEAQ65DrhY/AABmtznaiaEAg65Drhf/AAtzQINdJwSCRW49jINcLHyCCEGV4dG69IYIQc2ludL2wkl8D4IIQZXh0brqOtIAg1yEB0HTXIfpAMPpE+Cj6RDBYvZFb4O1E0IEBQdch9AWDB/QOb6ExkTDhgEDXIXB/2zzgMSDXSYECgLmRMOBw4hIRAeaO8O2i7fshgwjXIgKDCNcjIIAg1yHTH9Mf0x/tRNDSANMfINMf0//XCgAK+QFAzPkQmiiUXwrbMeHywIffArNQB7Dy0IRRJbry4IVQNrry4Ib4I7vy0IgikvgA3gGkf8jKAMsfAc8Wye1UIJL4D95w2zzYEgP27aLt+wL0BCFukmwhjkwCIdc5MHCUIccAs44tAdcoIHYeQ2wg10nACPLgkyDXSsAC8uCTINcdBscSwgBSMLDy0InXTNc5MAGk6GwShAe78uCT10rAAPLgk+1V4tIAAcAAkVvg69csCBQgkXCWAdcsCBwS4lIQseMPINdKFRQTABCTW9sx4ddM0AByMNcsCCSOLSHy4JLSAO1E0NIAURO68tCPVFAwkTGcAYEBQNch1woA8uCO4sjKAFjPFsntVJPywI3iAJYB+kAB+kT4KPpEMFi68uCR7UTQgQFB1xj0BQSdf8jKAEAEgwf0U/Lgi44UA4MH9Fvy4Iwi1woAIW4Bs7Dy0JDiyFADzxYS9ADJ7VSiwRtT"
        },
    },
    "dns.get_info": {
        "domain_name": "ness.ton",
    },
    "dns.resolve": {
        "domain_name": "ness.ton",
    },
    "dns.get_domain_bids": {
        "domain_name": "ness.ton",
    },
    "emulation.decode_message": {
        "body": {
            "boc": "te6ccgECGQEAA30AA+eIAAVfP1IB1faabWeSV4oC64cdA+yoEwkQ29KdZG8rDs6yEY5tLO3P///iP////+AAAAASpsVXwd0DY0bH1yDiWW7NOkqt/bGj96DxowrAtQqWLOhkB9YR1252BpE8UuwlCrV/AFKq3xqsoRSTgVZO6sl4LAEVFgEU/wD0pBP0vPLICwICASADDgIBSAQFAtzQINdJwSCRW49jINcLHyCCEGV4dG69IYIQc2ludL2wkl8D4IIQZXh0brqOtIAg1yEB0HTXIfpAMPpE+Cj6RDBYvZFb4O1E0IEBQdch9AWDB/QOb6ExkTDhgEDXIXB/2zzgMSDXSYECgLmRMOBw4hEQAgEgBg0CASAHCgIBbggJABmtznaiaEAg65Drhf/AABmvHfaiaEAQ65DrhY/AAgFICwwAF7Ml+1E0HHXIdcLH4AARsmL7UTQ1woAgABm+Xw9qJoQICg65D6AsAQLyDwEeINcLH4IQc2lnbrry4Ip/EAHmjvDtou37IYMI1yICgwjXIyCAINch0x/TH9Mf7UTQ0gDTHyDTH9P/1woACvkBQMz5EJoolF8K2zHh8sCH3wKzUAew8tCEUSW68uCFUDa68uCG+CO78tCIIpL4AN4BpH/IygDLHwHPFsntVCCS+A/ecNs82BED9u2i7fsC9AQhbpJsIY5MAiHXOTBwlCHHALOOLQHXKCB2HkNsINdJwAjy4JMg10rAAvLgkyDXHQbHEsIAUjCw8tCJ10zXOTABpOhsEoQHu/Lgk9dKwADy4JPtVeLSAAHAAJFb4OvXLAgUIJFwlgHXLAgcEuJSELHjDyDXShITFACWAfpAAfpE+Cj6RDBYuvLgke1E0IEBQdcY9AUEnX/IygBABIMH9FPy4IuOFAODB/Rb8uCMItcKACFuAbOw8tCQ4shQA88WEvQAye1UAHIw1ywIJI4tIfLgktIA7UTQ0gBRE7ry0I9UUDCRMZwBgQFA1yHXCgDy4I7iyMoAWM8Wye1Uk/LAjeIAEJNb2zHh10zQAFGAAAAAP///iMRfO4vi+c6oz+c8YmJcFTK52kRn5w2oJKa3Elti/RHOIAIKDsPIbQMXGAAAAJZCAAFXz9SAdX2mm1nkleKAuuHHQPsqBMJENvSnWRvKw7OsnMS0AAAAAAAAAAAAAAAAAAAAAAAASGVsbG8gZnJvbSB0b251dGlscyE="
        },
    },
    # "emulation.emulate_message_to_event": {
    #     "body": {"boc": ""},
    # },
    # "emulation.emulate_message_to_trace": {
    #     "body": {"boc": ""},
    # },
    # "emulation.emulate_message_to_wallet": {
    #     "body": {"boc": "", "params": [{"address": "0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b", "balance": 10000000000}]},
    # },
    # "emulation.emulate_message_to_account_event": {
    #     "account_id": "",
    #     "body": {"boc": ""},
    # },
    "events.get_event": {
        "event_id": "959ddd8cd66c7ebbe84d00676ddb6fa25ee90199413c467ccc1f25cb21fa0202",
    },
    # "events.emulate_message_to_event": {
    #     "body": {"boc": ""},
    # },
    "extra_currency.get_info": {
        "id": 239,
    },
    # "gasless.estimate": {
    #     "master_id": "",
    #     "body": {"throw_error_if_not_enough_jettons": False, "return_emulation": False, "wallet_address": "0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621", "wallet_public_key": "", "messages": [{"boc": ""}]},
    # },
    # "gasless.send": {
    #     "body": {"wallet_public_key": "", "boc": ""},
    # },
    "jettons.get_jetton_info": {
        "account_id": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
    },
    "jettons.get_jetton_infos_by_addresses": {
        "body": {"account_ids": ["EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs"]},
    },
    "jettons.get_jetton_holders": {
        "account_id": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
    },
    # "jettons.get_jetton_transfer_payload": {
    #     "account_id": "",
    #     "jetton_id": "",
    # },
    "jettons.get_events": {
        "event_id": "ea006561f153ef71597ae48150e84c59a1abc0488dcfab88d4a639e87224be3d",
    },
    "lite_server.get_raw_masterchain_info_ext": {
        "mode": 0,
    },
    "lite_server.get_raw_blockchain_block": {
        "block_id": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
    },
    # "lite_server.get_raw_blockchain_block_state": {
    #     "block_id": "",
    # },
    "lite_server.get_raw_blockchain_block_header": {
        "block_id": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
        "mode": 0,
    },
    # "lite_server.send_raw_message": {
    #     "body": {"body": ""},
    # },
    "lite_server.get_raw_account_state": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "lite_server.get_raw_shard_info": {
        "block_id": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
        "workchain": 0,
        "shard": 0,
        "exact": False,
    },
    "lite_server.get_all_raw_shards_info": {
        "block_id": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
    },
    # "lite_server.get_raw_transactions": {
    #     "account_id": "",
    #     "count": 0,
    #     "lt": 0,
    #     "hash": "",
    # },
    "lite_server.get_raw_list_block_transactions": {
        "block_id": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
        "mode": 0,
        "count": 10,
    },
    "lite_server.get_raw_block_proof": {
        "known_block": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
        "mode": 0,
    },
    "lite_server.get_raw_config": {
        "block_id": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
        "mode": 0,
    },
    "lite_server.get_raw_shard_block_proof": {
        "block_id": "(-1,8000000000000000,58001805,d9ac6be1c58065a92f88279c5947279f43845920cb2aa277e035ab7f985cecec,eb27e90a726866bd6b4700f9d00c38c795942895f0f3884ca84a0537f724a831)",
    },
    "migration.get_wallets": {
        "body": {"account_ids": ["UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0"]},
    },
    # "migration.prepare_migration": {
    #     "body": {"from": "0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621", "to": "0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621", "currency": "USD", "public_key": "29c1a72938b8f4f1d4e64f1e3f73e4b0e60f9b0c0e0d0e0f0a0b0c0d0e0f0a0b0", "gas_payer": "", "gas_jetton_master": "0:97264395BD65A255A429B11326C84128B7D70FFED7949ABAE3036D506BA38621"},
    # },
    # "multisig.get_account": {
    #     "account_id": "",
    # },
    # "multisig.get_order": {
    #     "account_id": "",
    # },
    "nft.get_account_nft_history": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
        "limit": 10,
    },
    "nft.get_collection": {
        "account_id": "EQC3dNlesgVD8YbAazcauIrXBPfiVhMMr5YYk2in0Mtsz0Bz",
    },
    "nft.get_collection_items_by_addresses": {
        "body": {"account_ids": ["EQC3dNlesgVD8YbAazcauIrXBPfiVhMMr5YYk2in0Mtsz0Bz"]},
    },
    "nft.get_items_from_collection": {
        "account_id": "EQC3dNlesgVD8YbAazcauIrXBPfiVhMMr5YYk2in0Mtsz0Bz",
    },
    "nft.get_items_by_addresses": {
        "body": {"account_ids": ["EQAMrsze7MaG_7P2ENd1eeT-S2VttJ1myT9sX5f-F1gY7xGx"]},
    },
    "nft.get_item_by_address": {
        "account_id": "EQAMrsze7MaG_7P2ENd1eeT-S2VttJ1myT9sX5f-F1gY7xGx",
    },
    "nft.get_history_by_id": {
        "account_id": "EQAMrsze7MaG_7P2ENd1eeT-S2VttJ1myT9sX5f-F1gY7xGx",
        "limit": 10,
    },
    "purchases.get_purchase_history": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "rates.get_rates": {
        "tokens": ["EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs"],
        "currencies": ["ton"],
    },
    "rates.get_chart_rates": {
        "token": "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",
    },
    # "staking.get_account_nominators_pools": {
    #     "account_id": "",
    # },
    # "staking.get_pool_info": {
    #     "account_id": "",
    # },
    # "staking.get_pool_history": {
    #     "account_id": "",
    # },
    "traces.get_trace": {
        "trace_id": "959ddd8cd66c7ebbe84d00676ddb6fa25ee90199413c467ccc1f25cb21fa0202",
    },
    # "traces.emulate_message_to_trace": {
    #     "body": {"boc": ""},
    # },
    "utilities.address_parse": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    # "wallet.ton_connect_proof": {
    #     "body": {"address": "0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b", "proof": {"timestamp": "1678275313", "domain": {"length_bytes": 0, "value": ""}, "signature": "", "payload": "84jHVNLQmZsAAAAAZB0Zryi2wqVJI-KaKNXOvCijEi46YyYzkaSHyJrMPBMOkVZa", "state_init": ""}},
    # },
    "wallet.get_account_seqno": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "wallet.get_info": {
        "account_id": "UQCDrgGaI6gWK-qlyw69xWZosurGxrpRgIgSkVsgahUtxZR0",
    },
    "wallet.get_wallets_by_public_key": {
        "public_key": "79c446597dbf81b9987e9059de95dc557bcd9e2c431a6db1677768783d0b99f7",
    },
    "wallet.get_wallets_by_public_key_bulk": {
        "body": {"public_keys": ["d8519b83d5b04b17a706ef6d04f3566422be47c2b676b0823235d67b1ef4b1b2"]},
    },
    # "wallet.emulate_message_to_wallet": {
    #     "body": {"boc": "", "params": [{"address": "0:97146a46acc2654y27947f14c4a4b14273e954f78bc017790b41208b0043200b", "balance": 10000000000}]},
    # },
}


def params(method: str) -> dict[str, object]:
    """Return test parameters for a given method.

    :param method: method key in ``"module.method_name"`` format.
    :return: dict of parameter names to values.
    """
    return TEST_DATA[method]
