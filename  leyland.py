import qrcode

# Leyland Cypress Tree Information
tree_info = """
Leyland Cypress Tree Information

Common Name: Leyland Cypress
Scientific Name: Cupressus × leylandii
Family: Cupressaceae

Leyland Cypress is a fast-growing evergreen tree.
It is widely used for hedges and privacy screens.
The tree can grow up to 60–70 feet tall.
It has soft green needle-like leaves and dense branches.

Benefits:
- Provides privacy and wind protection
- Fast growing ornamental tree
- Improves landscape beauty
"""

# Create QR code
qr = qrcode.make(tree_info)

# Save QR code image
qr.save("leyland_cypress_qrcode.png")

print("QR Code generated successfully!")
