from kivy.lang import Builder

# fmt: off
Builder.load_string("""
#:import rgba kivy.utils.get_color_from_hex

#:set slate_50 rgba("#f8fafc")
#:set slate_100 rgba("#f1f5f9")
#:set slate_200 rgba("#e2e8f0")
#:set slate_300 rgba("#cbd5e1")
#:set slate_400 rgba("#94a3b8")
#:set slate_500 rgba("#64748b")
#:set slate_600 rgba("#475569")
#:set slate_700 rgba("#334155")
#:set slate_800 rgba("#1e293b")
#:set slate_900 rgba("#0f172a")

#:set slate slate_500

#:set gray_50 rgba("#f9fafb")
#:set gray_100 rgba("#f3f4f6")
#:set gray_200 rgba("#e5e7eb")
#:set gray_300 rgba("#d1d5db")
#:set gray_400 rgba("#9ca3af")
#:set gray_500 rgba("#6b7280")
#:set gray_600 rgba("#4b5563")
#:set gray_700 rgba("#374151")
#:set gray_800 rgba("#1f2937")
#:set gray_900 rgba("#111827")

#:set gray gray_500

#:set zinc_50 rgba("#fafafa")
#:set zinc_100 rgba("#f4f4f5")
#:set zinc_200 rgba("#e4e4e7")
#:set zinc_300 rgba("#d4d4d8")
#:set zinc_400 rgba("#a1a1aa")
#:set zinc_500 rgba("#71717a")
#:set zinc_600 rgba("#52525b")
#:set zinc_700 rgba("#3f3f46")
#:set zinc_800 rgba("#27272a")
#:set zinc_900 rgba("#18181b")

#:set zinc zinc_500

#:set neutral_50 rgba("#fafafa")
#:set neutral_100 rgba("#f5f5f5")
#:set neutral_200 rgba("#e5e5e5")
#:set neutral_300 rgba("#d4d4d4")
#:set neutral_400 rgba("#a3a3a3")
#:set neutral_500 rgba("#737373")
#:set neutral_600 rgba("#525252")
#:set neutral_700 rgba("#404040")
#:set neutral_800 rgba("#262626")
#:set neutral_900 rgba("#171717")

#:set neutral neutral_500

#:set stone_50 rgba("#fafaf9")
#:set stone_100 rgba("#f5f5f4")
#:set stone_200 rgba("#e7e5e4")
#:set stone_300 rgba("#d6d3d1")
#:set stone_400 rgba("#a8a29e")
#:set stone_500 rgba("#78716c")
#:set stone_600 rgba("#57534e")
#:set stone_700 rgba("#44403c")
#:set stone_800 rgba("#292524")
#:set stone_900 rgba("#1c1917")

#:set stone stone_500

#:set red_50 rgba("#fef2f2")
#:set red_100 rgba("#fee2e2")
#:set red_200 rgba("#fecaca")
#:set red_300 rgba("#fca5a5")
#:set red_400 rgba("#f87171")
#:set red_500 rgba("#ef4444")
#:set red_600 rgba("#dc2626")
#:set red_700 rgba("#b91c1c")
#:set red_800 rgba("#991b1b")
#:set red_900 rgba("#7f1d1d")

#:set red red_500

#:set orange_50 rgba("#fff7ed")
#:set orange_100 rgba("#ffedd5")
#:set orange_200 rgba("#fed7aa")
#:set orange_300 rgba("#fdba74")
#:set orange_400 rgba("#fb923c")
#:set orange_500 rgba("#f97316")
#:set orange_600 rgba("#ea580c")
#:set orange_700 rgba("#c2410c")
#:set orange_800 rgba("#9a3412")
#:set orange_900 rgba("#7c2d12")

#:set orange orange_500

#:set amber_50 rgba("#fffbeb")
#:set amber_100 rgba("#fef3c7")
#:set amber_200 rgba("#fde68a")
#:set amber_300 rgba("#fcd34d")
#:set amber_400 rgba("#fbbf24")
#:set amber_500 rgba("#f59e0b")
#:set amber_600 rgba("#d97706")
#:set amber_700 rgba("#b45309")
#:set amber_800 rgba("#92400e")
#:set amber_900 rgba("#78350f")

#:set amber amber_500

#:set yellow_50 rgba("#fefce8")
#:set yellow_100 rgba("#fef9c3")
#:set yellow_200 rgba("#fef08a")
#:set yellow_300 rgba("#fde047")
#:set yellow_400 rgba("#facc15")
#:set yellow_500 rgba("#eab308")
#:set yellow_600 rgba("#ca8a04")
#:set yellow_700 rgba("#a16207")
#:set yellow_800 rgba("#854d0e")
#:set yellow_900 rgba("#713f12")

#:set yellow yellow_500

#:set lime_50 rgba("#f7fee7")
#:set lime_100 rgba("#ecfccb")
#:set lime_200 rgba("#d9f99d")
#:set lime_300 rgba("#bef264")
#:set lime_400 rgba("#a3e635")
#:set lime_500 rgba("#84cc16")
#:set lime_600 rgba("#65a30d")
#:set lime_700 rgba("#4d7c0f")
#:set lime_800 rgba("#3f6212")
#:set lime_900 rgba("#365314")

#:set lime lime_500

#:set green_50 rgba("#f0fdf4")
#:set green_100 rgba("#dcfce7")
#:set green_200 rgba("#bbf7d0")
#:set green_300 rgba("#86efac")
#:set green_400 rgba("#4ade80")
#:set green_500 rgba("#22c55e")
#:set green_600 rgba("#16a34a")
#:set green_700 rgba("#15803d")
#:set green_800 rgba("#166534")
#:set green_900 rgba("#14532d")

#:set green green_500

#:set emerald_50 rgba("#ecfdf5")
#:set emerald_100 rgba("#d1fae5")
#:set emerald_200 rgba("#a7f3d0")
#:set emerald_300 rgba("#6ee7b7")
#:set emerald_400 rgba("#34d399")
#:set emerald_500 rgba("#10b981")
#:set emerald_600 rgba("#059669")
#:set emerald_700 rgba("#047857")
#:set emerald_800 rgba("#065f46")
#:set emerald_900 rgba("#064e3b")

#:set emerald emerald_500

#:set teal_50 rgba("#f0fdfa")
#:set teal_100 rgba("#ccfbf1")
#:set teal_200 rgba("#99f6e4")
#:set teal_300 rgba("#5eead4")
#:set teal_400 rgba("#2dd4bf")
#:set teal_500 rgba("#14b8a6")
#:set teal_600 rgba("#0d9488")
#:set teal_700 rgba("#0f766e")
#:set teal_800 rgba("#115e59")
#:set teal_900 rgba("#134e4a")

#:set teal teal_500

#:set cyan_50 rgba("#ecfeff")
#:set cyan_100 rgba("#cffafe")
#:set cyan_200 rgba("#a5f3fc")
#:set cyan_300 rgba("#67e8f9")
#:set cyan_400 rgba("#22d3ee")
#:set cyan_500 rgba("#06b6d4")
#:set cyan_600 rgba("#0891b2")
#:set cyan_700 rgba("#0e7490")
#:set cyan_800 rgba("#155e75")
#:set cyan_900 rgba("#164e63")

#:set cyan cyan_500

#:set sky_50 rgba("#f0f9ff")
#:set sky_100 rgba("#e0f2fe")
#:set sky_200 rgba("#bae6fd")
#:set sky_300 rgba("#7dd3fc")
#:set sky_400 rgba("#38bdf8")
#:set sky_500 rgba("#0ea5e9")
#:set sky_600 rgba("#0284c7")
#:set sky_700 rgba("#0369a1")
#:set sky_800 rgba("#075985")
#:set sky_900 rgba("#0c4a6e")

#:set sky sky_500

#:set blue_50 rgba("#eff6ff")
#:set blue_100 rgba("#dbeafe")
#:set blue_200 rgba("#bfdbfe")
#:set blue_300 rgba("#93c5fd")
#:set blue_400 rgba("#60a5fa")
#:set blue_500 rgba("#3b82f6")
#:set blue_600 rgba("#2563eb")
#:set blue_700 rgba("#1d4ed8")
#:set blue_800 rgba("#1e40af")
#:set blue_900 rgba("#1e3a8a")

#:set blue blue_500

#:set indigo_50 rgba("#eef2ff")
#:set indigo_100 rgba("#e0e7ff")
#:set indigo_200 rgba("#c7d2fe")
#:set indigo_300 rgba("#a5b4fc")
#:set indigo_400 rgba("#818cf8")
#:set indigo_500 rgba("#6366f1")
#:set indigo_600 rgba("#4f46e5")
#:set indigo_700 rgba("#4338ca")
#:set indigo_800 rgba("#3730a3")
#:set indigo_900 rgba("#312e81")

#:set indigo indigo_500

#:set violet_50 rgba("#f5f3ff")
#:set violet_100 rgba("#ede9fe")
#:set violet_200 rgba("#ddd6fe")
#:set violet_300 rgba("#c4b5fd")
#:set violet_400 rgba("#a78bfa")
#:set violet_500 rgba("#8b5cf6")
#:set violet_600 rgba("#7c3aed")
#:set violet_700 rgba("#6d28d9")
#:set violet_800 rgba("#5b21b6")
#:set violet_900 rgba("#4c1d95")

#:set violet violet_500

#:set purple_50 rgba("#faf5ff")
#:set purple_100 rgba("#f3e8ff")
#:set purple_200 rgba("#e9d5ff")
#:set purple_300 rgba("#d8b4fe")
#:set purple_400 rgba("#c084fc")
#:set purple_500 rgba("#a855f7")
#:set purple_600 rgba("#9333ea")
#:set purple_700 rgba("#7e22ce")
#:set purple_800 rgba("#6b21a8")
#:set purple_900 rgba("#581c87")

#:set purple purple_500

#:set fuchsia_50 rgba("#fdf4ff")
#:set fuchsia_100 rgba("#fae8ff")
#:set fuchsia_200 rgba("#f5d0fe")
#:set fuchsia_300 rgba("#f0abfc")
#:set fuchsia_400 rgba("#e879f9")
#:set fuchsia_500 rgba("#d946ef")
#:set fuchsia_600 rgba("#c026d3")
#:set fuchsia_700 rgba("#a21caf")
#:set fuchsia_800 rgba("#86198f")
#:set fuchsia_900 rgba("#701a75")

#:set fuchsia fuchsia_500

#:set pink_50 rgba("#fdf2f8")
#:set pink_100 rgba("#fce7f3")
#:set pink_200 rgba("#fbcfe8")
#:set pink_300 rgba("#f9a8d4")
#:set pink_400 rgba("#f472b6")
#:set pink_500 rgba("#ec4899")
#:set pink_600 rgba("#db2777")
#:set pink_700 rgba("#be185d")
#:set pink_800 rgba("#9d174d")
#:set pink_900 rgba("#831843")

#:set pink pink_500

#:set rose_50 rgba("#fff1f2")
#:set rose_100 rgba("#ffe4e6")
#:set rose_200 rgba("#fecdd3")
#:set rose_300 rgba("#fda4af")
#:set rose_400 rgba("#fb7185")
#:set rose_500 rgba("#f43f5e")
#:set rose_600 rgba("#e11d48")
#:set rose_700 rgba("#be123c")
#:set rose_800 rgba("#9f1239")
#:set rose_900 rgba("#881337")

#:set rose rose_500

#:set white rgba("#ffffff")
#:set black rgba("#000000")
#:set transparent rgba("#00000000")
""")
# fmt: on
